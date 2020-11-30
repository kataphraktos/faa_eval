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
        print_file.write_result_csv(self.faa_test, self.local_result_path)
        self.assertEqual('1', self.faa_test)

    def test_webfiles(self):
        print_file.write_webfiles(self.faa_test, self.local_result_path)
        self.assertEqual('1', self.faa_test)

if __name__ == '__main__':
    unittest.main()