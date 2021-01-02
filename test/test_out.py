import unittest
import os
import sys
import pickle
import csv
TESTPATH = os.path.dirname(os.path.realpath(__file__))
FAAPATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
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
        #write csv of results
        print_file.write_result_csv(cls.faa_test, cls.local_result_path)
        #print all web files - individual tests check for certain files
        print_file.write_webfiles(cls.faa_test, cls.local_result_path)

    def test_csv_results(self):
        res = []
        with open(os.path.join(self.local_result_path, "results.csv")) as resf:
            res_reader = csv.reader(resf)
            for row in res_reader:
                res.append(row[1])
        self.assertEqual(["Need to File?", "Yes", "No", "Yes"], res)

    def test_res_page(self):
        res = []
        res_path = [
            os.path.join(self.local_result_path, "1.html"),
            os.path.join(self.local_result_path, "1_1.html"),
            os.path.join(self.local_result_path, "Turbine #3.html")
            ]
        for run_path in res_path:
            res.append(os.path.exists(run_path))
        self.assertEqual([True, True, True], res)

    def test_webfiles(self):
        res = []
        res_path = [
            os.path.join(self.local_result_path, "oeaaa", "external", "images", "favicon.png"),
            os.path.join(self.local_result_path, "oeaaa", "external", "images", "layout", "head_logo_left.gif"),
            os.path.join(self.local_result_path, "oeaaa", "external", "include", "css", "oeaaaExternal.css")
        ]
        for run_path in res_path:
            res.append(os.path.exists(run_path))
        self.assertEqual([True, True, True], res)

if __name__ == '__main__':
    unittest.main()