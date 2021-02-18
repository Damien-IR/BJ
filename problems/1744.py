from collections import deque
from sys import stdin


def solution(arr):
    q = deque(sorted(arr))
    result = 0
    while len(q) >= 2 and q[-1] > 0 and q[-2] > 0:
        a, b = q.pop(), q.pop()
        result += a * b if a * b >= a + b else a + b
    while len(q) >= 2 and q[0] < 0 and q[1] < 0:
        a, b = q.popleft(), q.popleft()
        result += a * b if a * b >= a + b else a + b
    while len(q) >= 2 and q[0] < 0 and q[1] == 0:
        result += q.popleft() * q.popleft()

    result += sum(q)
    return result


n = int(stdin.readline())
array = [int(stdin.readline().strip()) for _ in range(n)]
print(solution(array))


# 28
print(solution([-5, -2, -1, 0, 3, 6]))
# 48
print(solution([3, 9, 4, 3, 3]))
# 3
print(solution([1, 2]))
# 245
print(solution([-10, -9, -8, -7, -6, -5, 1, 2, 3, 4, 5, 6, 7]))
# 65
print(solution([-5, -4, -3, 0, 1, 2, 3, 4, 5, 6]))
# 2
print(solution([-1, -2, 0, 0, 0]))
# 25
print(solution([-5, -4, -3, -2, -1]))
# 5
print(solution([1, 1, 1, 1, 1]))
# 8
print(solution([-3, -2, -1, 1, 2]))
# 29
print(solution([-6, -5, -1]))
# 65
print(solution([-5, -4, -3, 0, 1, 2, 3, 4, 5, 6]))
# 8
print(solution([-3, -2, -1, 1, 2]))
# 1
print(solution([-1, 0, 1]))
