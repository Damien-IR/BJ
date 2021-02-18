def solution(p):
    d = dict()
    for index, item in enumerate(p):
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    a = [list(i) for i in sorted(d.items(), key=lambda x: x[0])]
    m = max(a, key=lambda x: x[1])[1]
    count = 0
    for i in range(m, 0, -1):
        tmp = 10000000
        for j in range(len(a)):
            if a[j][1] == i:
                if tmp < a[j][0]:
                    count += 1
                tmp = a[j][0]
                a[j][1] -= 1
    return count


print(solution([3, 2, 1, 4, 5]))
print(solution([20, 10, 10, 20]))
print(solution([103, 101, 103, 103, 101, 102, 100, 100, 101, 104]))
