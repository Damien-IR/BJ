def solution(str1, str2):
    a, b = [[0 for i in range(26)] for j in range(2)]
    result = 0
    count(a, str1), count(b, str2)
    for i in range(len(a)):
        result += abs(a[i] - b[i])
    return result


def count(rst, string):
    for char in string:
        rst[ord(char) - 97] += 1


print(solution(input(), input()))

print(solution('aabbcc', 'xxyybb'))
