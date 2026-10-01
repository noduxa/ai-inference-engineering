import copy
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
import validate_learning as v
spec=importlib.util.spec_from_file_location('lab',ROOT/'phase-2/scripts/inference_lab.py')
lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)

class CurriculumTests(unittest.TestCase):
 def setUp(self):
  self.r=v.load_registry(ROOT/'phase-2/sources.yaml');self.c=v.load_registry(ROOT/'phase-2/curriculum.yaml')
 def check(self,word):self.assertTrue(any(word in e for e in v.validate_phase(self.r,self.c,'phase-2')))
 def test_valid(self):self.assertEqual(v.validate_phase(self.r,self.c,'phase-2'),[])
 def test_missing_source(self):self.c['modules'][0]['source_ids'][0]='absent';self.check('missing source')
 def test_unused_source(self):self.c['modules'][0]['source_ids'].pop();self.check('unused source')
 def test_missing_metadata(self):self.r['sources'][0].pop('skip_sections');self.check('skip_sections')
 def test_duplicate_global(self):self.assertTrue(v.duplicate_ids([self.r,self.r]))
 def test_missing_curriculum(self):self.assertTrue(v.validate_phase(self.r,None,'phase-2'))
 def test_malformed_module(self):self.c['modules'][0]=None;self.check('module mappings')
 def test_bad_reference_type(self):self.c['modules'][0]['source_ids']=[{}];self.check('reference type')
 def test_bad_prerequisite(self):self.c['modules'][0]['prerequisites']=['P2-M07'];self.check('prerequisite')
 def test_invalid_status(self):self.c["modules"][0]["status"]=[];self.check("learner status")
 def test_missing_assessment(self):self.c['modules'][0]['assessment_ids']=['missing'];self.check('assessment')
 def test_bad_hours(self):self.c['modules'][0]['estimated_hours']=True;self.check('hours')
 def test_bad_session_hours(self):self.c['weeks'][0]['sessions'][0]['hours']=4;self.check('15 hours')
 def test_bad_next(self):self.c['modules'][0]['next_module']='P2-M07';self.check('next_module')
 def test_missing_evidence(self):self.c['modules'][0].pop('evidence_requirements');self.check('evidence_requirements')
 def test_links(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'a.md').write_text('# A\n\n[bad](missing.md)\n');errors,count=v.internal_links(root)
   self.assertEqual(len(errors),1);self.assertEqual(count,0)

class LabTests(unittest.TestCase):
 def test_cache_gqa(self):self.assertEqual(lab.kv_bytes(12,3,512,2,64,2),9437184)
 def test_cache_invalid(self):
  for x in (0,-1,1.5,True):
   with self.assertRaises(ValueError):lab.kv_bytes(x,1,1,1,1,2)
 def test_metrics(self):
  r=lab.token_metrics(0,[.4,.5,.7,1],1.1)
  self.assertAlmostEqual(r['tpot_s'],.2);self.assertEqual(r['ttft_s'],.4)
 def test_single_token(self):self.assertIsNone(lab.token_metrics(0,[1],2)['tpot_s'])
 def test_bad_clock(self):
  for stamps in ([],[2,1],[float('nan')]):
   with self.assertRaises(ValueError):lab.token_metrics(0,stamps,3)
 def test_small_tail(self):self.assertIsNone(lab.summarize([1,2,3])['p95_nearest_rank'])
 def test_nearest_rank(self):self.assertEqual(lab.summarize(list(range(1,21)))['p95_nearest_rank'],19)
 def test_invalid_samples(self):
  for x in ([],[-1],[float('inf')]):
   with self.assertRaises(ValueError):lab.summarize(x)
 def test_budget(self):
  r=lab.budget_study();self.assertFalse(r['physical_oom']);self.assertFalse(r['rows'][-1]['accepted'])
 def test_budget_cli_no_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'result.json';self.assertEqual(lab.main(['--budget-only','--out',str(p)]),0)
   with self.assertRaises(SystemExit):lab.main(['--budget-only','--out',str(p)])

if __name__=='__main__':unittest.main()
