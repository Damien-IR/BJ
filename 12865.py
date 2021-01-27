import sys
from itertools import combinations


def solution(n, k, arr):
    result = 0
    for i in range(n + 1):
        for j in list(combinations(arr, i)):
            tmp = arr_sum(list(j))
            if tmp[0] <= k:
                result = max(result, tmp[1])
    return result


def arr_sum(arr):
    result = [0, 0]
    for i, v in arr:
        result[0] += i
        result[1] += v
    return result


n, k = [int(i) for i in input().strip().split()]
array = []
for i in range(n):
    array.append([int(j) for j in input().strip().split()])
print(solution(n, k, array))

# 14
# print(solution(4, 7, [[6, 13], [4, 8], [3, 6], [5, 12]]))
#
