from sys import stdin


def solution(n):
    cache = [1] * 10
    for i in range(n):
        add = 0
        array = []
        for j in range(-1, -11, -1):
            add += cache[j]
            array.append(add)
        cache += array[::-1]
    return cache[-10] % 10007


print(solution(int(stdin.readline())))

print(solution(1))
print(solution(2))
print(solution(3))