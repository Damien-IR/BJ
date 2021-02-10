from bisect import bisect


# https://drops.dagstuhl.de/opus/volltexte/2018/8491/pdf/LIPIcs-STACS-2018-44.pdf 참조
def solution(arr: list) -> list:
    cache: list = [[] for i in range(len(arr) + 1)]
    cache[0].append(1001)
    pos, j = 0, 0
    for val in reversed(arr):
        if val < cache[pos][-1]:
            pos += 1
            cache[pos] = list()
            j = pos
        else:
            for tmp in range(0, pos + 1):
                if val > cache[tmp][-1]:
                    j = tmp
                    break
        cache[j].append(val)
    result: list = [min(cache[pos])]
    for i in range(pos - 1, 0, -1):
        next_pos: int = bisect(cache[i], result[-1])
        if next_pos < len(cache[i]):
            result.append(cache[i][next_pos])
    return result


def solve(k: int = int(input()), arr=None):
    if arr is None:
        arr = list(map(int, input().split()))
    result: list = solution(arr)
    print(len(result))
    print(*result)


solve()

# 1
# 2, 3
# 10, 20, 30, 50
# 2, 4, 5, 7
# 1, 2, 4, 5, 7
# 1, 2, 3, 4
# 1, 2, 5, 10
solve(1, [1])
solve(3, [3, 2, 3])
solve(6, [10, 20, 10, 30, 20, 50])
solve(9, [2, 8, 4, 9, 5, 1, 7, 6, 3])
solve(7, [1, 6, 2, 4, 5, 3, 7])
solve(6, [1, 5, 6, 2, 3, 4])
solve(7, [1, 7, 3, 2, 5, 10, 3])
