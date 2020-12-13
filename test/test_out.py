import unittest
import os
import sys
import pickle
TESTPATH = os.path.dirname(os.path.abspath(__file__))
FAAPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, FAAPATH)
from src import utils, faa_web, print_file

class Test_output_writer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local_result_path = os.path.join(TESTPATH, '.result')
        faa_test_path = os.path.join(cls.local_result_path, 'faa_web_test.pkl')
        with open(faa_test_path, 'rb') as in_test:
            faa_test = pickle.load(in_test)
        cls.faa_test = faa_test

    def test_results(self):
        res = []
        print_file.write_result_csv(self.faa_test, self.local_result_path)
        res_path = [os.path.join(self.local_result_path, "1.html"),
            os.path.join(self.local_result_path, "1_1.html"),
            os.path.join(self.local_result_path, "Turbine #3.html")]
        for run_path in res_path:
            res.append(os.path.exists(run_path))
        self.assertEqual([True, True, True], res)

    def test_webfiles(self):
        print_file.write_webfiles(self.faa_test, self.local_result_path)
        res_path = os.path.join(self.local_result_path, "oeaaa", "external", "images", "favicon.png")
        self.assertEqual(True, os.path.exists(res_path))

if __name__ == '__main__':
    unittest.main()