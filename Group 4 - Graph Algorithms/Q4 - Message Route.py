# https://cses.fi/problemset/task/1667
# BFS shortest path + path reconstruction, 7-10p
#
# To reconstruct, we track the node that we arrived from
#
# TC: O(n + m)

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

prev = [-1] * (n + 1)
prev[1] = 0
q = deque([1])
while q:
    cur = q.popleft()
    for adj in graph[cur]:
        if prev[adj] != -1:
            continue
        prev[adj] = cur
        q.append(adj)

if prev[-1] == -1:
    print("IMPOSSIBLE")
else:
    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    print(len(path))
    print(" ".join(map(str, path)))
