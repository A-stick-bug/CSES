# https://cses.fi/problemset/task/1668
# Bipartite graph coloring, 7-10p
#
# Adjacent nodes must be in different groups, this is the classic 2 coloring problem
# We can use either BFS or DFS, flipping the group number at every edge
# If we contradict a previous result, it must be impossible
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

color = [-1] * (n + 1)


def color_component(start):
    stack = [start]
    color[start] = 0
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if color[adj] != -1:  # previously visited, ensure no contradiction
                if color[adj] == color[cur]:
                    print("IMPOSSIBLE")
                    sys.exit()
                continue
            else:
                color[adj] = color[cur] ^ 1
                stack.append(adj)


for i in range(1, n + 1):
    if color[i] == -1:
        color_component(i)

print(" ".join(map(lambda x: str(x + 1), color[1:])))
