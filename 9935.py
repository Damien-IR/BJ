def solution(string, bomb):
    bomb_len = len(bomb)
    answer = []

    for char in string:
        answer += char
        answer_len = len(answer)
        while answer_len > 0 and answer[-1] == bomb[-1] and ''.join(answer[max(answer_len - bomb_len, 0):]) == bomb:
            for _ in range(bomb_len):
                answer.pop()
            answer_len = len(answer)

    return 'FRULA' if len(answer) == 0 else ''.join(answer)


# s = input().strip()
# b = input().strip()
# print(solution(s, b))
#
print(solution("mirkovC4nizCC44", "C4"))
print(solution("12ab112ab2ab", "12ab"))
print(solution("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", "9fpOlYimF5xbtkvnDu4c68ZjR") + '\n')
