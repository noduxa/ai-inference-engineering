"""Small random-model integration checks; no downloads and no performance assertions."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/'inference_lab.py'
spec=importlib.util.spec_from_file_location('lab',SCRIPT)
lab=importlib.util.module_from_spec(spec);spec.loader.exec_module(lab)
AVAILABLE=importlib.util.find_spec('torch') and importlib.util.find_spec('transformers')

@unittest.skipUnless(AVAILABLE,'Install requirements-lab.txt for model integration tests')
class ModelIntegration(unittest.TestCase):
 def run_lab(self,path,*args):
  self.assertEqual(lab.main(['--toy','--fixed-output','--runs','2','--warmup','0','--output-tokens','4','--out',str(path),*args]),0)
  return json.loads(path.read_text())
 def test_cache_equivalence_and_clock_contract(self):
  with tempfile.TemporaryDirectory() as d:
   cached=self.run_lab(Path(d)/'cached.json')
   uncached=self.run_lab(Path(d)/'uncached.json','--no-cache')
   for a,b in zip(cached['requests'],uncached['requests']):
    self.assertEqual(a['selected_ids'],b['selected_ids'])
    self.assertEqual(a['completion_tokens_per_sequence'],4)
    self.assertEqual(len(a['metrics']['itl_s']),3)
    self.assertGreaterEqual(a['submitted_e2e_s'],a['metrics']['e2e_s'])
    self.assertGreaterEqual(a['metrics']['e2e_s'],a['metrics']['ttft_s'])
 def test_batch_and_concurrency_counts(self):
  with tempfile.TemporaryDirectory() as d:
   r=self.run_lab(Path(d)/'batch.json','--batch','2','--concurrency','2')
   self.assertEqual(len(r['requests']),2)
   self.assertEqual(sum(len(t) for x in r['requests'] for t in x['selected_ids']),16)
   self.assertAlmostEqual(r['summary']['output_tokens_per_s']*r['summary']['window_s'],16)
 def test_dtype_payload(self):
  with tempfile.TemporaryDirectory() as d:
   a=self.run_lab(Path(d)/'fp32.json')
   b=self.run_lab(Path(d)/'fp64.json','--dtype','float64')
   self.assertEqual(b['metadata']['parameter_payload_bytes'],2*a['metadata']['parameter_payload_bytes'])

if __name__=='__main__':unittest.main()
