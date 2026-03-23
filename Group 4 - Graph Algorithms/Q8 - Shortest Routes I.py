# https://cses.fi/problemset/task/1671
# Template Dijkstra's algorithm, 10p
#
# TC: O(M log M)

import sys
from heapq import heappush, heappop

inf = 1 << 60
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

pq = [(0, 1)]
dist = [inf] * (N + 1)
dist[1] = 0
while pq:
    d, cur = heappop(pq)
    if d > dist[cur]:
        continue
    for adj, adj_d in graph[cur]:
        new_d = d + adj_d
        if new_d < dist[adj]:
            dist[adj] = new_d
            heappush(pq, (new_d, adj))

print(" ".join(map(str, dist[1:])))
