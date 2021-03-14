from sys import stdin


def solution(tape_l: int, positions: list[int]) -> int:
    positions.sort()
    count: int = 0
    pos: int = 0
    next_pos: int = pos
    if len(positions) == 1:
        return 1
    while pos < len(positions):
        if next_pos >= len(positions):
            count += 1
            break
        elif abs(positions[pos] - positions[next_pos]) + 1 > tape_l:
            pos = next_pos
            count += 1
        else:
            next_pos += 1
    return count


def solve():
    n, l = map(int, stdin.readline().strip().split())
    leak_points: list = list(map(int, stdin.readline().strip().split()))
    print(solution(l, leak_points))


solve()

# from unittest import TestCase
#
# from problems.BJ1449 import solution
#
#
# class T1449(TestCase):
#     def test1(self):
#         self.assertEqual(solution(1, [1, 2, 3, 4, 5]), 5)
#
#     def test2(self):
#         self.assertEqual(solution(3, [1, 2, 3, 4]), 2)
#
#     def test3(self):
#         self.assertEqual(solution(2, [1, 2, 3, 4, 5]), 3)
#
#     def test4(self):
#         self.assertEqual(solution(3, [1, 2, 3, 4, 1000]), 3)
#
#     def test5(self):
#         self.assertEqual(solution(1000, [1, 1000]), 1)
