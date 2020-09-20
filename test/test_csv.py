#unit tests for parsing csvs and related functions

import unittest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import utils

class Test_coord_to_dms(unittest.TestCase):
    def test_Sformats(self):
        South_res = [65, 30, 48.60000, "S"]
        self.assertEqual(utils.coord_to_dms("-65.5135", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("65.5135S", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("65d30'48.6\"S", "lat"), South_res)
        self.assertEqual(utils.coord_to_dms("-65d30'48.6\"", "lat"), South_res)
    def test_Wformats(self):
        West_res = [103, 15, 55.67983, "W"]
        self.assertEqual(utils.coord_to_dms("-103.2654666194", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("103.2654666194W", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("103 d 15'55.67983\"W", "long"), West_res)
        self.assertEqual(utils.coord_to_dms("-103 d 15'55.67983\"", "long"), West_res)
    def test_other_directions(self):
        self.assertEqual(utils.coord_to_dms("85", "lat"), [85, 0, 0.00000, "N"])
        self.assertEqual(utils.coord_to_dms("103.2654666194", "long"), [103, 15, 55.67983, "E"])



if __name__ == '__main__':
    unittest.main()