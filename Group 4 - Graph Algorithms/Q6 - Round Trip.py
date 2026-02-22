# https://cses.fi/problemset/task/1669
# DFS Cycle detection, 10p
#
# This is the classic cycle detection problem.
# The algorithm works by contradiction: imagine there are no cycles (i.e. it is a tree)
# Here, we should never encounter a previously visited node if we use DFS
# So if we do, we must have a contradiction and the graph is not a tree (has a cycle)
#
# note:
# - we can easily extract the nodes in the cycle by tracking the current dfs path
# - this is significantly simpler when implemented recursively
#
# TC: O(n + m)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200_000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

path = []  # current path
vis = [False] * (n + 1)


def dfs(cur, prev):
    path.append(cur)
    if vis[cur]:  # cycle
        cycle = path[path.index(cur):]
        print(len(cycle))
        print(" ".join(map(str, cycle)))
        sys.exit()

    vis[cur] = True

    for adj in graph[cur]:
        if adj == prev:
            continue
        dfs(adj, cur)
    path.pop()


for i in range(1, n + 1):
    if not vis[i]:
        dfs(i, -1)

print("IMPOSSIBLE")
