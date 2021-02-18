from sys import stdin


def solution(n):
    cache = [1, 1, 1]
    while len(cache) < n:
        cache.append(cache[-2] + cache[-3])
    return cache[-1]


n = int(stdin.readline())
for i in range(n):
    print(solution(int(stdin.readline())))

print(solution(6))
print(solution(12))
