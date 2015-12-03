__author__ = 'fabienlamarque'

import unittest
from src.exercice1 import calculatestairs
from src.exercice1 import basemententrance
from utils.FileReader import readfile


class Exercice1Test(unittest.TestCase):
    def test_testFramework(self):
        self.assertEquals(0, 0)

    def test_unit(self):
        self.assertEquals(calculatestairs(""), 0)

    def test_upstairs(self):
        self.assertEquals(calculatestairs("("), 1)

    def test_downstairs(self):
        self.assertEquals(calculatestairs(")"), -1)

    def test_two_stairs_up_one_stair_down(self):
        self.assertEquals(calculatestairs("(()"), 1)

    def test_calculate_stairs_with_file(self):
        self.assertEquals(calculatestairs(readfile("resources/1x1.txt")), 280)

    def test_direct_basement_entrance(self):
        self.assertEquals(basemententrance(")"), 1)

    def test_basement_third_step(self):
        self.assertEquals(basemententrance("())"), 3)

    def test_basement_entrance_with_file(self):
        self.assertEquals(basemententrance(readfile("resources/1x1.txt")), 1797)



if __name__ == '__main__':
    unittest.main()
