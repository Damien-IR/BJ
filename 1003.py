from sys import stdin


def solution(n):
    a, b = 1, 0
    for i in range(n):
        tmp = a + b
        a = b
        b = tmp
    return str(a) + ' ' + str(b)


t = int(stdin.readline())
for i in range(t):
    print(solution(i))
