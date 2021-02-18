from sys import stdin


def solution(string1, string2):
    cache = [[0 for i in range(len(string2) + 1)] for i in range(len(string1) + 1)]
    for i, s1 in enumerate(string1):
        for j, s2 in enumerate(string2):
            if s1 == s2:
                cache[i + 1][j + 1] = cache[i][j] + 1
            else:
                cache[i + 1][j + 1] = max(cache[i + 1][j], cache[i][j + 1])
    return cache[len(string1)][len(string2)]


print(solution(stdin.readline().strip(), stdin.readline().strip()))

# 4 31 1 200 10 10 13
# 4
print(solution("ACAYKP", "CAPCAK"))
# 31
print(solution("AACGGAACACGCTTTAAGGGCGATGGAATACCGTGGGTTTACCTAAAACTA", "AATCTGGCCTATTCTGGGTCAAATGGCGTGAGCAAACATCGTACA"))
# 1
print(solution("CAPCK", "AA"))
# 200
print(solution(
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
# 10
print(solution("SKDFHWEODJKSFSDFJK", "WKJSDHFOWEFKJDVKSDF"))
# 10
print(solution("KJSDFKSDFLKDFJS", "SKDJKFLSKDJFLKSDJF"))
# 13
print(solution("LKSDJFLKJWPOJSDLKJFSDF", "OISJDKFJLKEJFSLKJDIFJSLDK"))
