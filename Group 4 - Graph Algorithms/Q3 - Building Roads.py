# https://cses.fi/problemset/task/1666
# Flood fill/DFS, 7-10p
#
# Originally, the graph may be many connected components
# Let component 1 be the 'root' and connect a node from every other component to it
# This is optimal (think of building a tree with components as nodes)
#
# TC: O(n + m)

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [False] * (n + 1)


def visit_component(start):  # mark the component from `start` as visited
    stack = [start]
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not vis[adj]:
                vis[adj] = True
                stack.append(adj)


comps = []  # contains nodes that represent each component
for i in range(1, n + 1):
    if not vis[i]:
        comps.append(i)
        visit_component(i)

print(len(comps) - 1)
for c in comps[1:]:
    print(comps[0], c)
