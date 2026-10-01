#!/usr/bin/env python3
"""Validate the source registry; optionally inspect public HTTP endpoints.

Offline: python phase-1/scripts/validate_sources.py
Online:  python phase-1/scripts/validate_sources.py --http --timeout 15
Install the sole dependency from scripts/requirements.txt in a virtual environment.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
from html.parser import HTMLParser
import ipaddress
import json
from pathlib import Path
import re
import socket
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

try:
    import yaml
except ImportError:
    raise SystemExit("Install PyYAML: python -m pip install -r phase-1/scripts/requirements.txt")

REQUIRED = {
    "id", "module", "title", "url", "publisher", "authors", "source_type",
    "authority_level", "required_or_optional", "exact_sections", "estimated_hours",
    "access", "format", "published_or_updated", "license_or_terms",
    "notebooklm_compatible", "reason_selected", "last_verified", "status",
}
DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "sources.yaml"


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently overwriting them."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            if key in result:
                raise ValueError(f"Duplicate YAML key: {key}")
            result[key] = loader.construct_object(value_node, deep=deep)
        except TypeError as exc:
            raise ValueError("YAML mapping keys must be scalar") from exc
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_registry(path):
    with Path(path).open(encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueLoader)


def valid_url(value):
    if not isinstance(value, str) or re.search(r"\s", value):
        return False
    try:
        parsed = urlsplit(value)
        return bool(
            parsed.scheme in {"http", "https"} and parsed.hostname
            and "." in parsed.hostname and not parsed.username and not parsed.password
            and parsed.port in {None, 80, 443}
        )
    except ValueError:
        return False


def valid_date(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate_registry(document):
    errors = []
    if not isinstance(document, dict) or type(document.get("schema_version")) is not int or document.get("schema_version") != 1:
        return ["Root must be a mapping with schema_version: 1"]
    sources = document.get("sources")
    if not isinstance(sources, list) or not sources:
        return ["sources must be a non-empty list"]
    seen = set()
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label}: expected a mapping")
            continue
        label = str(source.get("id", label))
        for field in sorted(REQUIRED):
            if field not in source or source[field] is None or source[field] == "":
                errors.append(f"{label}: missing/empty {field}")
        source_id = source.get("id")
        if not isinstance(source_id, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", source_id):
            errors.append(f"{label}: invalid id")
        elif source_id in seen:
            errors.append(f"{label}: duplicate source id")
        else:
            seen.add(source_id)
        if type(source.get("module")) is not int or source["module"] not in range(1, 8):
            errors.append(f"{label}: module must be an integer from 1 to 7")
        if not valid_url(source.get("url")):
            errors.append(f"{label}: invalid public HTTP(S) URL")
        value = source.get("estimated_hours")
        if type(value) not in (float, int) or not 0 < value < 100:
            errors.append(f"{label}: estimated_hours must be a positive finite number below 100")
        authors = source.get("authors")
        if not isinstance(authors, list) or not authors or not all(isinstance(a, str) and a.strip() for a in authors):
            errors.append(f"{label}: authors must be a non-empty string list")
        for field in REQUIRED - {"module", "estimated_hours", "authors", "exact_sections"}:
            if field in source and (not isinstance(source[field], str) or not source[field].strip()):
                errors.append(f"{label}: {field} must be a non-empty string")
        if source.get("required_or_optional") not in ("required", "optional"):
            errors.append(f"{label}: required_or_optional must be required or optional")
        if source.get("access") not in ("free", "registration required", "paid"):
            errors.append(f"{label}: unsupported access type")
        if source.get("status") not in ("Verified", "To be validated", "Restricted", "Stale"):
            errors.append(f"{label}: unsupported source status")
        if not valid_date(source.get("last_verified")):
            errors.append(f"{label}: last_verified must be a quoted YYYY-MM-DD date")
        sections = source.get("exact_sections")
        if not isinstance(sections, list) or not sections:
            errors.append(f"{label}: exact_sections must be a non-empty list")
            continue
        for section in sections:
            if not isinstance(section, dict):
                errors.append(f"{label}: each section must be a mapping")
                continue
            for field in ("title", "study", "skip"):
                if not isinstance(section.get(field), str) or not section[field].strip():
                    errors.append(f"{label}: section requires {field}")
            if not valid_url(section.get("url")):
                errors.append(f"{label}: invalid section URL")
    return errors


def public_endpoint(url):
    """Reject local/private destinations, including redirect targets."""
    if not valid_url(url):
        raise ValueError("Not a supported public HTTP(S) URL")
    parsed = urlsplit(url)
    addresses = socket.getaddrinfo(parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
    if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
        raise ValueError("Refusing a non-public network destination")


class PublicRedirect(HTTPRedirectHandler):
    max_redirections = 5

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_endpoint(newurl)
        if req.full_url.startswith("https:") and not newurl.startswith("https:"):
            raise ValueError("Refusing HTTPS downgrade")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class RefreshParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.target = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            match = re.search(r"url\s*=\s*(.+)$", attrs.get("content", ""), re.I)
            if match:
                self.target = match.group(1).strip(" '\"")


def check_url(url, timeout=15, opener=None, guard=public_endpoint):
    """Bounded GET detects content stubs that a successful HEAD can miss.

    No cookies, login, scripts or response bodies are persisted. HTTP blocks and
    transport errors remain distinct from malformed registry data.
    """
    opener = opener or build_opener(PublicRedirect())
    current = url
    visited = set()
    try:
        for _ in range(6):
            if current in visited:
                return {"url": url, "status": "inaccessible", "detail": "redirect loop"}
            visited.add(current)
            guard(current)
            request = Request(current, headers={"User-Agent": "Phase1-source-validator/1.0"})
            with opener.open(request, timeout=timeout) as response:
                final = response.geturl()
                data = response.read(32768).decode("utf-8", errors="replace")
                code = response.status
            parser = RefreshParser()
            parser.feed(data)
            if parser.target:
                target = urljoin(final, parser.target)
                if final.startswith("https:") and not target.startswith("https:"):
                    raise ValueError("Refusing HTTPS downgrade")
                current = target
                continue
            lower = data.lower()
            if any(marker in lower for marker in ("<title>just a moment", "<title>access denied", "<title>sign in")):
                return {"url": url, "status": "blocked", "detail": "access/login challenge", "final_url": final}
            if "doesn't exist in" in lower and "documentation" in lower and "redirect" in lower:
                return {"url": url, "status": "inaccessible", "detail": "documentation-version redirect notice; inspect canonical page", "final_url": final}
            if "<title>redirecting" in lower:
                return {"url": url, "status": "inaccessible", "detail": "unresolved redirect stub", "final_url": final}
            return {"url": url, "status": "reachable" if final == url and current == url else "redirected", "http": code, "final_url": final}
        return {"url": url, "status": "inaccessible", "detail": "redirect limit exceeded"}
    except HTTPError as exc:
        result = {"url": url, "status": "blocked" if exc.code in {401, 403, 429} else "inaccessible", "http": exc.code, "detail": str(exc.reason)}
        exc.close()
        return result
    except (URLError, TimeoutError, OSError) as exc:
        return {"url": url, "status": "unverified", "detail": str(exc)}
    except ValueError as exc:
        return {"url": url, "status": "inaccessible", "detail": str(exc)}


def registry_urls(document):
    return sorted({u for s in document["sources"] for u in [s["url"], *(sec["url"] for sec in s["exact_sections"])]})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", nargs="?", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--http", action="store_true", help="Check exact pages with bounded public GETs")
    parser.add_argument("--strict-http", action="store_true", help="Exit 1 for inaccessible links; implies --http")
    parser.add_argument("--timeout", type=float, default=15, help="Per-request timeout in seconds (default 15)")
    parser.add_argument("--json", type=Path, help="Write HTTP results to a JSON file")
    args = parser.parse_args(argv)
    if not 0 < args.timeout <= 60:
        parser.error("--timeout must be greater than 0 and at most 60")
    try:
        document = load_registry(args.registry)
        errors = validate_registry(document)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAIL: {len(errors)} registry error(s)", file=sys.stderr)
        return 2
    sources = document["sources"]
    print(f"PASS: {len(sources)} source collections, {len(registry_urls(document))} unique URLs")
    print("Collections by module: " + ", ".join(f"{k}: {v}" for k, v in sorted(Counter(s['module'] for s in sources).items())))
    if not (args.http or args.strict_http):
        print("HTTP checks not requested; source currency requires manual content review.")
        return 0
    results = []
    for url in registry_urls(document):
        result = check_url(url, args.timeout)
        results.append(result)
        print(f"{result['status'].upper()}: {url}", flush=True)
    summary = dict(Counter(r["status"] for r in results))
    print("HTTP summary: " + json.dumps(summary, sort_keys=True))
    print("Access blocks/timeouts require manual review; HTTP success does not prove content relevance.")
    if args.json:
        args.json.write_text(json.dumps({"summary": summary, "results": results}, indent=2) + "\n", encoding="utf-8")
    return int(args.strict_http and any(r["status"] == "inaccessible" for r in results))


if __name__ == "__main__":
    raise SystemExit(main())
