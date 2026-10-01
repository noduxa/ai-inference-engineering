"""Offline regression tests for malformed data and HTTP classification."""
import copy
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate_sources as validator


class RegistryTests(unittest.TestCase):
    def setUp(self):
        source = validator.load_registry(validator.DEFAULT_REGISTRY)["sources"][0]
        self.doc = {"schema_version": 1, "sources": [copy.deepcopy(source)]}

    def test_valid(self):
        self.assertEqual(validator.validate_registry(self.doc), [])

    def test_missing_each_required_field(self):
        for field in validator.REQUIRED:
            with self.subTest(field=field):
                doc = copy.deepcopy(self.doc)
                del doc["sources"][0][field]
                self.assertTrue(validator.validate_registry(doc))

    def test_duplicate_ids(self):
        self.doc["sources"] *= 2
        self.assertTrue(any("duplicate source id" in e for e in validator.validate_registry(self.doc)))

    def test_bad_roots(self):
        for value in (None, [], {}, {"schema_version": 1, "sources": []}):
            self.assertTrue(validator.validate_registry(value))

    def test_nonmapping_source(self):
        self.doc["sources"] = [None]
        self.assertTrue(validator.validate_registry(self.doc))

    def test_malformed_values(self):
        for field, value in [("module", True), ("module", 8), ("authors", []), ("estimated_hours", float("nan")), ("estimated_hours", -1), ("title", []), ("last_verified", "2026-02-30"), ("exact_sections", []), ("exact_sections", ["section"]), ("access", "unknown"), ("status", []), ("required_or_optional", {})]:
            with self.subTest(field=field, value=value):
                doc = copy.deepcopy(self.doc)
                doc["sources"][0][field] = value
                self.assertTrue(validator.validate_registry(doc))

    def test_section_fields(self):
        for field in ("url", "title", "study", "skip"):
            doc = copy.deepcopy(self.doc)
            del doc["sources"][0]["exact_sections"][0][field]
            self.assertTrue(validator.validate_registry(doc))

    def test_url_formats(self):
        for value in (None, "file:///tmp/test", "https://", "https://example.com/a b", "https://u:p@example.com", "https://example.com:invalid", "https://example.com:8080"):
            self.assertFalse(validator.valid_url(value))
        self.assertTrue(validator.valid_url("https://example.com/doc?a=b#section"))

    def test_duplicate_yaml_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.yaml"
            path.write_text("schema_version: 1\nschema_version: 2\n")
            with self.assertRaises(ValueError):
                validator.load_registry(path)

    def test_cli_malformed_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.yaml"
            path.write_text("sources: [")
            with patch("sys.stderr", new=io.StringIO()):
                self.assertEqual(validator.main([str(path)]), 2)

    def test_cli_offline_no_network(self):
        with patch.object(validator, "check_url") as check, patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(validator.main([]), 0)
            check.assert_not_called()


    def test_strict_http_inaccessible_exit(self):
        with patch.object(validator, "registry_urls", return_value=["https://example.com/doc"]), patch.object(validator, "check_url", return_value={"url": "https://example.com/doc", "status": "inaccessible"}), patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(validator.main(["--strict-http"]), 1)

    def test_access_block_does_not_fail_strict_mode(self):
        with patch.object(validator, "registry_urls", return_value=["https://example.com/doc"]), patch.object(validator, "check_url", return_value={"url": "https://example.com/doc", "status": "blocked"}), patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(validator.main(["--strict-http"]), 0)

    def test_invalid_yaml_tag_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unsafe.yaml"
            path.write_text("!!python/object:builtins.object {}")
            with self.assertRaises(validator.yaml.YAMLError):
                validator.load_registry(path)


class HTTPTests(unittest.TestCase):
    def response(self, body=b"<h1>Useful page</h1>", url="https://example.com/doc"):
        response = Mock()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        response.geturl.return_value = url
        response.status = 200
        response.read.return_value = body
        return response

    def check(self, opener):
        return validator.check_url("https://example.com/doc", opener=opener, guard=lambda url: None)

    def test_reachable_and_bounded_read(self):
        response = self.response()
        result = self.check(Mock(open=Mock(return_value=response)))
        self.assertEqual(result["status"], "reachable")
        response.read.assert_called_once_with(32768)

    def test_http_redirect(self):
        result = self.check(Mock(open=Mock(return_value=self.response(url="https://example.com/new"))))
        self.assertEqual(result["status"], "redirected")

    def test_meta_redirect(self):
        first = self.response(b'<meta http-equiv="refresh" content="0; url=/new">')
        opener = Mock(open=Mock(side_effect=[first, self.response(url="https://example.com/new")]))
        self.assertEqual(self.check(opener)["status"], "redirected")

    def test_redirect_loop(self):
        first = self.response(b'<meta http-equiv="refresh" content="0; url=/doc">')
        self.assertEqual(self.check(Mock(open=Mock(return_value=first)))["detail"], "redirect loop")

    def test_http_errors(self):
        for code, status in [(403, "blocked"), (429, "blocked"), (404, "inaccessible"), (500, "inaccessible")]:
            with self.subTest(code=code):
                opener = Mock(open=Mock(side_effect=HTTPError("https://example.com/doc", code, "test", {}, None)))
                self.assertEqual(self.check(opener)["status"], status)

    def test_transport_error(self):
        for error in (URLError("timeout"), TimeoutError("timed out")):
            self.assertEqual(self.check(Mock(open=Mock(side_effect=error)))["status"], "unverified")

    def test_challenge_and_unresolved_stub(self):
        for body, status in [(b"<title>Just a moment</title>", "blocked"), (b"<title>Redirecting</title>", "inaccessible")]:
            self.assertEqual(self.check(Mock(open=Mock(return_value=self.response(body))))["status"], status)

    def test_documentation_version_notice(self):
        body = b"The documentation page doesn't exist in this version. Click to redirect."
        result = self.check(Mock(open=Mock(return_value=self.response(body))))
        self.assertEqual(result["status"], "inaccessible")
        self.assertIn("version", result["detail"])

    def test_https_downgrade(self):
        first = self.response(b'<meta http-equiv="refresh" content="0; url=http://example.com/new">')
        self.assertIn("downgrade", self.check(Mock(open=Mock(return_value=first)))["detail"])

    def test_private_destination(self):
        with patch.object(validator.socket, "getaddrinfo", return_value=[(2, 1, 6, "", ("127.0.0.1", 443))]):
            with self.assertRaisesRegex(ValueError, "non-public"):
                validator.public_endpoint("https://example.com/doc")

    def test_redirect_guard(self):
        request = validator.Request("https://example.com/doc")
        with patch.object(validator, "public_endpoint", side_effect=ValueError("non-public")):
            with self.assertRaises(ValueError):
                validator.PublicRedirect().redirect_request(request, None, 302, "", {}, "https://example.net/new")


if __name__ == "__main__":
    unittest.main()
