#!/usr/bin/env python3
"""Validate both learning phases and repository links; optionally check public URLs."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'phase-1/scripts'))
from validate_sources import load_registry,validate_registry,registry_urls,check_url
from validate_harness import markdown_text
import re
from urllib.parse import urlsplit,unquote

EXTRA_FIELDS=('skip_sections','expected_learning','verification_status')
MODULE_FIELDS=('id','title','status','objectives','prerequisites','source_ids','exercises',
               'assessment_ids','estimated_hours','scheduled_week','evidence_requirements',
               'exit_criteria','next_module','guide','source_pack')
STATUSES={'Planned','Not started','In progress','To be validated','Completed'}


def validate_phase(registry,curriculum,phase):
    """Pure structural/reference checks; no network or file access."""
    errors=validate_registry(registry)
    if errors:return [f'{phase}: {e}' for e in errors]
    sources={s['id']:s for s in registry['sources']}
    for sid,s in sources.items():
        for field in EXTRA_FIELDS:
            if not isinstance(s.get(field),str) or not s[field].strip():errors.append(f'{sid}: missing/invalid {field}')
    if not isinstance(curriculum,dict):return errors+[f'{phase}: curriculum must be a mapping']
    if curriculum.get('schema_version') != 1: errors.append(f'{phase}: unsupported curriculum schema')
    modules=curriculum.get('modules');assessments=curriculum.get('assessments')
    if not isinstance(modules,list) or len(modules)!=7 or any(not isinstance(m,dict) for m in modules):return errors+[f'{phase}: expected seven module mappings']
    if not isinstance(assessments,list) or any(not isinstance(a,dict) or not isinstance(a.get('id'),str) for a in assessments):return errors+[f'{phase}: invalid assessments']
    aids=[a['id'] for a in assessments]
    if len(aids)!=len(set(aids)):errors.append(f'{phase}: duplicate assessment IDs')
    used=set();seen=set();hours=0
    for index,m in enumerate(modules):
        mid=m.get('id',f'index {index}')
        for f in MODULE_FIELDS:
            if f not in m or m[f] is None or m[f]=='':errors.append(f'{mid}: missing {f}')
        if not isinstance(mid,str):errors.append('Invalid module ID');continue
        if mid in seen:errors.append(f'{mid}: duplicate module ID')
        for f in ('objectives','prerequisites','source_ids','assessment_ids','evidence_requirements','exit_criteria','scheduled_week','exercises'):
            if not isinstance(m.get(f),list):errors.append(f'{mid}: {f} must be a list')
        if any(not isinstance(m.get(f),list) for f in ('prerequisites','source_ids','assessment_ids','exercises')):continue
        if any(not isinstance(v,str) for f in ('prerequisites','source_ids','assessment_ids') for v in m[f]):errors.append(f'{mid}: invalid reference type');continue
        allowed=seen|({'phase-1:exit-gate'} if phase=='phase-2' and index==0 else set())
        if not set(m['prerequisites'])<=allowed:errors.append(f'{mid}: unknown/out-of-order prerequisite')
        seen.add(mid)
        if not isinstance(m.get('status'),str) or m.get('status') not in STATUSES:errors.append(f'{mid}: invalid learner status')
        if not set(m['assessment_ids'])<=set(aids):errors.append(f'{mid}: unknown assessment')
        for sid in m['source_ids']:
            used.add(sid)
            if sid not in sources:errors.append(f'{mid}: missing source {sid}')
            elif sources[sid]['module']!=index+1:errors.append(f'{mid}: wrong source module {sid}')
        mapped=[sources[s] for s in m['source_ids'] if s in sources]
        if sum(s.get('role')=='primary' for s in mapped)!=1:errors.append(f'{mid}: require one primary source')
        if not 2<=sum(s.get('role')=='supporting' for s in mapped)<=4:errors.append(f'{mid}: require two to four supporting sources')
        h=m.get('estimated_hours')
        if type(h) not in (int,float) or not 0<h<100:errors.append(f'{mid}: invalid hours')
        else:
            hours+=h
            if sum(s['estimated_hours'] for s in mapped)>=h:errors.append(f'{mid}: no practice time')
        expected=modules[index+1].get('id') if index<6 else ('phase-2:P2-M01' if phase=='phase-1' else 'phase-3:community-entry')
        if m.get('next_module')!=expected:errors.append(f'{mid}: next_module inconsistent')
        for e in m['exercises']:
            if not isinstance(e,dict) or not isinstance(e.get('id'),str) or not isinstance(e.get('path'),str):errors.append(f'{mid}: invalid exercise reference')
    for sid in sources.keys()-used:errors.append(f'{phase}: unused source {sid}')
    total=90 if phase=='phase-1' else 60;count=6 if phase=='phase-1' else 4
    final=curriculum.get('final_assessment_hours')
    if type(final) not in (int,float) or hours+final!=total or curriculum.get('total_hours')!=total:errors.append(f'{phase}: hour budget must total {total}')
    if curriculum.get('module_hours')!=hours:errors.append(f'{phase}: module_hours mismatch')
    weeks=curriculum.get('weeks')
    if not isinstance(weeks,list) or len(weeks)!=count:return errors+[f'{phase}: expected {count} weeks']
    for w in weeks:
        if not isinstance(w,dict) or not isinstance(w.get('sessions'),list):errors.append(f'{phase}: malformed week');continue
        sessions=w['sessions']
        if any(not isinstance(s,dict) or type(s.get('hours')) not in (int,float) or s['hours']<=0 for s in sessions):errors.append(f'{phase}: malformed session');continue
        if w.get('hours')!=15 or sum(s['hours'] for s in sessions)!=15:errors.append(f'{phase}: week must total 15 hours')
        for s in sessions:
            for f in ('objective','practice','evidence','review_questions'):
                if not s.get(f):errors.append(f'{phase}: session missing {f}')
            for sid in s.get('source_ids',[]):
                if sid not in sources:errors.append(f'{phase}: session missing source {sid}')
    return errors


def duplicate_ids(registries):
    ids=[s['id'] for r in registries for s in r.get('sources',[]) if isinstance(s,dict) and isinstance(s.get('id'),str)]
    return [f'Duplicate cross-phase source ID: {sid}' for sid,n in Counter(ids).items() if n>1]


def internal_links(root):
    errors=[];count=0
    for path in sorted(root.rglob('*.md')):
        if any(p in {'.git','.venv','node_modules','outputs'} for p in path.parts):continue
        text=markdown_text(path)
        targets=re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)',text)+re.findall(r'^\[[^\]]+\]:\s*(\S+)',text,re.M)
        for target in targets:
            parsed=urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:continue
            dest=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.is_file():errors.append(f'{path.relative_to(root)}: broken link {target}');continue
            if parsed.fragment:
                heads=re.findall(r'^#+\s+(.+)$',markdown_text(dest),re.M)
                anchors={re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in heads}
                if unquote(parsed.fragment) not in anchors:errors.append(f'{path.relative_to(root)}: unknown anchor {target}')
            count+=1
    return errors,count


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--http',action='store_true');p.add_argument('--timeout',type=float,default=15)
    p.add_argument('--json',type=Path);a=p.parse_args(argv)
    if not 0<a.timeout<=60:p.error('timeout must be in (0,60]')
    errors=[];docs={};registries=[]
    for path in sorted([*ROOT.rglob('*.yaml'),*ROOT.rglob('*.yml')]):
        if any(x in {'.git','.venv','node_modules','outputs'} for x in path.parts):continue
        try:docs[path]=load_registry(path)
        except Exception as exc:errors.append(f'{path.relative_to(ROOT)}: malformed YAML: {exc}')
    for phase in ('phase-1','phase-2'):
        base=ROOT/phase;r=docs.get(base/'sources.yaml');c=docs.get(base/'curriculum.yaml')
        phase_errors=validate_phase(r,c,phase);errors.extend(phase_errors)
        if phase_errors:continue
        registries.append(r);sources={s['id']:s for s in r['sources']}
        for m in c['modules']:
            for key in ('guide','source_pack'):
                if not (base/m[key]).is_file():errors.append(f'{phase}: missing {m[key]}')
            pack=(base/m['source_pack']).read_text() if (base/m['source_pack']).is_file() else ''
            for sid in m['source_ids']:
                for url in registry_urls({'sources':[sources[sid]]}):
                    if url not in pack:errors.append(f'{m["id"]}: source pack missing URL {url}')
            for e in m['exercises']:
                if not (base/e['path']).is_file():errors.append(f'{phase}: missing exercise {e["path"]}')
            if m['status']=='Completed':
                ev=m.get('evidence',[])
                if not ev or not all(isinstance(v,str) and (base/v).is_file() for v in ev):errors.append(f'{m["id"]}: completion requires evidence files')
        for assessment in c['assessments']:
            if not isinstance(assessment.get('path'),str) or not (base/assessment['path']).is_file():errors.append(f'{phase}: missing assessment file')
    errors.extend(duplicate_ids(registries));link_errors,links=internal_links(ROOT);errors.extend(link_errors)
    if errors:
        for e in errors:print('ERROR:',e,file=sys.stderr)
        print(f'FAIL: {len(errors)} structural/link errors');return 2
    print(f'PASS: {len(docs)} YAML files; 14 modules; Phase 1 90 h; Phase 2 60 h; {links} internal links')
    print(f'PASS: {sum(len(r["sources"]) for r in registries)} source records, references, evidence fields and schedules')
    if a.http:
        urls=sorted({u for r in registries for u in registry_urls(r)});results=[]
        for url in urls:
            result=check_url(url,a.timeout);results.append(result);print(result['status'].upper(),url,flush=True)
        report={'summary':dict(Counter(r['status'] for r in results)),'results':results}
        print('HTTP:',report['summary']);print('HTTP success is not content inspection; blocks/timeouts require manual review.')
        if a.json:a.json.write_text(json.dumps(report,indent=2)+'\n')
    return 0

if __name__=='__main__':raise SystemExit(main())
