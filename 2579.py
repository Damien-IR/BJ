from collections import deque

n = int(input())
q = deque()
for i in range(n):
    q.append(int(input()))
dp = deque()

if n >= 1:
    dp.append(q[0])
if n >= 2:
    dp.append(max(q[0] + q[1], q[1]))
if n >= 3:
    dp.append(max(q[0] + q[2], q[1] + q[2]))
    for i in range(3, n):
        dp.append(max(dp[i - 3] + q[i - 1] + q[i], dp[i - 2] + q[i]))

print(dp.pop())
