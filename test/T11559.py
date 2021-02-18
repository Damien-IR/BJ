from unittest import TestCase

from problems.BJ11559 import *


class T11559(TestCase):
    def test_bomb(self):
        sets: set = set()
        for i in range(2):
            for j in range(2):
                sets.add((i, j))
        self.assertEqual(bomb(sets, [['2', '2'], ['2', '2']]), [])

    def test1(self):
        tmp: list = [['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', 'R', '.'],
                     ['.', 'Y', '.', '.', 'P', '.'],
                     ['.', 'G', '.', '.', 'P', 'R'],
                     ['R', 'R', 'Y', 'Y', 'Y', 'R'],
                     ['R', 'R', 'G', 'G', 'G', 'R']]
        self.assertEqual(solution(tmp), 3)
