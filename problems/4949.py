def solution(string):
    answer = []
    braces = ['[', ']', '(', ')']
    bomb = ['[]', '()']
    for char in string:
        # print(answer, char)
        if char in braces:
            answer.append(char)
        if len(answer) >= 2:
            while ''.join(answer[-2:]) in bomb:
                for i in range(2):
                    answer.pop()
    return 'yes' if len(answer) == 0 else 'no'


while True:
    text = input()
    if text == '.':
        break
    print(solution(text))

# print(solution("So when I die (the [first] I will see in (heaven) is a score list)."))
# print(solution("[ first in ] ( first out )."))
# print(solution("Half Moon tonight (At least it is better than no Moon at all]."))
# print(solution("A rope may form )( a trail in a maze."))
# print(solution("Help( I[m being held prisoner in a fortune cookie factory)]."))
# print(solution("([ (([( [ ] ) ( ) (( ))] )) ])."))
# print(solution(" ."))
