from collections import deque

x = int(input())
q = deque()
count = 0

q.append([x, 0])

while len(q) > 0:
    n, c = q.popleft()
    if n == 1:
        count = c
        break
    if n % 3 == 0:
        q.append([n // 3, c + 1])
    if n % 2 == 0:
        q.append([n // 2, c + 1])
    q.append([n - 1, c + 1])

print(count)
