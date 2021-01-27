from sys import stdin


def solution(n):
    cache = [1, 3, 5, 11]
    if n < 2:
        return n
    while len(cache) <= n:
        cache.append(cache[-2] * 2 + cache[-1])
    return cache[n-1] % 10007


print(solution(int(stdin.readline())))

for i in range(0, 13):
    print(i, solution(i))