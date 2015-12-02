__author__ = 'fabienlamarque'

import unittest
from src.exercice1 import calculatestairs
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

    def test_file_reading(self):
        self.assertEquals(calculatestairs(readfile("resources/1x1.txt")), 280)


if __name__ == '__main__':
    unittest.main()
