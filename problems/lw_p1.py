from collections import deque


def solution(a, b, c, d, e, f):
    sf = a + b + c
    sb = d + e + f
    if sf - sb >= 2:
        return True
    else:
        q = deque()
        q.append((a, b, c, sf - sb))
        while len(q) > 0:
            x, y, z, count = q.popleft()
            if x == d and y == e and z == f:
                return True
            if count == 0:
                return False
            if x >= 2:
                q.append((x - 2, y + 1, z, count - 1))
                q.append((x - 2, y, z + 1, count - 1))
            if y >= 2:
                q.append((x + 1, y - 2, z, count - 1))
                q.append((x, y - 2, z + 1, count - 1))
            if z >= 2:
                q.append((x, y + 1, z - 2, count - 1))
                q.append((x + 1, y, z - 2, count - 1))
        return False


print(solution(4, 4, 0, 2, 1, 2))
print(solution(3, 3, 3, 2, 2, 2))
print(solution(2, 2, 1, 1, 1, 2))
print(solution(2, 4, 3, 2, 4, 2))
