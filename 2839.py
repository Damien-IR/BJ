def solution(n):
    q, r = n // 5, n % 5
    for i in range(q, -1, -1):
        tmp = n - 5 * i
        if tmp % 3 == 0:
            return i + tmp // 3
    return -1


print(solution(int(input())))

# 4
print(solution(18))
# -1
print(solution(4))
# 2
print(solution(6))
# 3
print(solution(9))
# 3
print(solution(11))
# 7
print(solution(27))
