def solution(n, m, string):
    pn_length = 2 * n + 1
    count, i = 0, 0
    while i <= m - pn_length:
        if string[i] == 'I':
            tmp = 0
            while string[i + tmp + tmp + 1: i + tmp + tmp + 3] == 'OI':
                tmp += 1
            if tmp >= n:
                count += tmp - n + 1
                i += tmp + tmp
            else:
                i += tmp + tmp + 1
        else:
            i += 1
    return count


print(solution(int(input()), int(input()), input()))


# print(solution(1, 13, "OOIOIOIOIIOII"))
# print(solution(2, 25, "OOIOIIOIOIOIOIOIOIOIOOIOI"))
# print(solution(1, 6, "IOIOOI"))
