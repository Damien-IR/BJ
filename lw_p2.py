def solution(arr):
    dup = dict()
    for index, item in enumerate(arr):
        if item not in dup:
            dup[item] = [index]
        else:
            dup[item].append(index)
    result = 100001
    for value in dup.values():
        if len(value) >= 2:
            for i in range(len(value) - 1):
                result = min(result, value[i + 1] - value[i])
    return -1 if result == 100001 else result


print(solution([2, 1, 3, 1, 4, 2, 1, 3]))
print(solution([1, 2, 3]))
