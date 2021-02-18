from collections import deque

q = deque()
n = int(input())
nc = int(input())
nodes = [set() for i in range(n)]
affected = [False] * n
for i in range(nc):
    start, end = [int(i) for i in input().split()]
    nodes[start - 1].add(end - 1)
    nodes[end - 1].add(start - 1)

affected[0] = True
q.append(0)
while len(q) > 0:
    point = q.popleft()
    for node in nodes[point]:
        if not affected[node]:
            affected[node] = True
            q.append(node)

count = 0
for i in range(1, n):
    if affected[i]:
        count += 1

print(count)
