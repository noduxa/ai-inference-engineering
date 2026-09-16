#!/usr/bin/env python3
"""Check YAML references, 90-hour accounting and repository Markdown links offline."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from validate_sources import load_registry, validate_registry

ROOT = Path(__file__).resolve().parents[2]
PHASE = ROOT / 'phase-1'


def markdown_text(path):
    text = path.read_text(encoding='utf-8')
    # Code examples are not navigation links.
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def check_harness():
    errors = []
    yaml_paths = sorted([*ROOT.rglob('*.yaml'), *ROOT.rglob('*.yml')])
    documents = {}
    for path in yaml_paths:
        if '.git' in path.parts or '.venv' in path.parts:
            continue
        try:
            documents[path] = load_registry(path)
        except Exception as exc:
            errors.append(f'{path.relative_to(ROOT)}: invalid YAML: {exc}')
    sources_doc = documents.get(PHASE / 'sources.yaml')
    errors.extend(validate_registry(sources_doc))
    curriculum = documents.get(PHASE / 'curriculum.yaml')
    if errors or not isinstance(curriculum, dict):
        return errors or ['Missing curriculum mapping'], 0, len(documents)
    sources = {s['id']: s for s in sources_doc['sources']}
    modules = curriculum.get('modules', [])
    if len(modules) != 7:
        errors.append('Expected seven modules')
    module_ids = [m['id'] for m in modules]
    if len(set(module_ids)) != len(module_ids):
        errors.append('Duplicate module IDs')
    assessment_ids = {a['id'] for a in curriculum['assessments']}
    exercise_ids = set()
    seen = set()
    for module in modules:
        mid = module['id']
        for field in ('objectives', 'required_concepts', 'source_ids', 'exercises', 'assessment_ids', 'exit_criteria', 'scheduled_week'):
            if not module.get(field):
                errors.append(f'{mid}: empty {field}')
        if module['status'] not in ('Planned', 'Not started', 'In progress', 'To be validated', 'Completed'):
            errors.append(f'{mid}: unknown learner status')
        if module['status'] == 'Completed':
            evidence = module.get('evidence', [])
            if not evidence or not all(isinstance(item, str) and (PHASE / item).is_file() for item in evidence):
                errors.append(f'{mid}: completion requires existing evidence files')
        if not set(module['prerequisites']).issubset(seen):
            errors.append(f'{mid}: prerequisite missing or out of order')
        seen.add(mid)
        if not set(module['assessment_ids']).issubset(assessment_ids):
            errors.append(f'{mid}: unknown assessment')
        module_sources = []
        pack = PHASE / module['source_pack']
        pack_text = pack.read_text() if pack.is_file() else ''
        for sid in module['source_ids']:
            if sid not in sources:
                errors.append(f'{mid}: unknown source {sid}')
                continue
            source = sources[sid]
            module_sources.append(source)
            if source['module'] != module['number']:
                errors.append(f'{mid}: source {sid} mapped to wrong module')
            for url in [source['url'], *(section['url'] for section in source['exact_sections'])]:
                if url not in pack_text:
                    errors.append(f'{mid}: source pack missing exact URL from {sid}: {url}')
        if sum(s.get('role') == 'primary' for s in module_sources) != 1:
            errors.append(f'{mid}: expected one primary source')
        if sum(s.get('role') == 'supporting' for s in module_sources) > 3:
            errors.append(f'{mid}: too many supporting sources')
        if sum(s['estimated_hours'] for s in module_sources) >= module['estimated_hours']:
            errors.append(f'{mid}: no time remains for exercises')
        for path in (module['guide'], module['source_pack']):
            if not (PHASE / path).is_file():
                errors.append(f'{mid}: missing {path}')
        for section in ('Module purpose', 'Learning objectives', 'Prerequisites', 'Ordered source table', 'Initial NotebookLM questions', 'Audio Overview customization prompt', 'Study-guide generation prompt', 'Flashcard-generation prompt', 'Quiz-generation prompt', 'Common misconceptions to test', 'Practical exercise', 'Required learning evidence', 'Exit criteria', 'What to study next'):
            if f'## {section}' not in pack_text:
                errors.append(f'{mid}: missing pack section {section}')
        for exercise in module['exercises']:
            eid = exercise['id']
            if eid in exercise_ids:
                errors.append(f'Duplicate exercise ID {eid}')
            exercise_ids.add(eid)
            path = PHASE / exercise['path']
            if not path.is_file() or eid not in path.read_text():
                errors.append(f'{eid}: missing exercise specification')
    for assessment in curriculum['assessments']:
        if not (PHASE / assessment['path']).is_file():
            errors.append(f"Missing assessment: {assessment['id']}")
    module_hours = sum(m['estimated_hours'] for m in modules)
    weeks = curriculum.get('weeks', [])
    if module_hours != 88 or curriculum.get('final_assessment_hours') != 2 or curriculum.get('total_hours') != 90:
        errors.append('Expected 88 module hours + 2 final assessment hours = 90')
    if len(weeks) != 6 or sum(w['hours'] for w in weeks) != 90:
        errors.append('Expected six weeks totaling 90 hours')
    for week in weeks:
        if week['hours'] != 15 or sum(s['hours'] for s in week['sessions']) != 15:
            errors.append(f"Week {week['week']}: sessions must total 15 hours")
    if curriculum.get('target_date') != '2026-10-31':
        errors.append('Unexpected Phase 1 target date')
    links = 0
    for path in sorted(ROOT.rglob('*.md')):
        if any(p in {'.git', '.venv', 'node_modules'} for p in path.parts):
            continue
        text = markdown_text(path)
        targets = re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', text)
        targets += re.findall(r'^\[[^\]]+\]:\s*(\S+)', text, flags=re.M)
        for target in targets:
            target = target.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not destination.is_relative_to(ROOT) or not destination.is_file():
                errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
                continue
            if parsed.fragment:
                headings = re.findall(r'^#+\s+(.+)$', markdown_text(destination), flags=re.M)
                anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(parsed.fragment) not in anchors:
                    errors.append(f'{path.relative_to(ROOT)}: unknown anchor {target}')
            links += 1
    return errors, links, len(documents)


def main():
    errors, links, documents = check_harness()
    if errors:
        for error in errors:
            print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print(f'PASS: {documents} YAML files; 7 modules; 90 hours; {links} internal Markdown links')
    print('PASS: source-pack URLs, prerequisites, exercises, assessments and learning statuses')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
