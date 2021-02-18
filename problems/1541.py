from sys import stdin


def solution(string):
    result = 0
    for i, s in enumerate(string.split('-')):
        tmp = 0
        for t in s.split('+'):
            tmp += int(t)
        if i == 0:
            result += tmp
        else:
            result -= tmp

    return result


print(solution(stdin.readline().strip()))

# print(solution("0+50-40-25+40-125"))
