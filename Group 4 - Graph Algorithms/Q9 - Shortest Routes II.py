# TLE, CHECK C++ CODE
#
# https://cses.fi/problemset/task/1672
# Template Floyd-Warshall algorithm, 10-12p
#
# TC: O(n^3 + m + q)

import sys


def solve():
    input = sys.stdin.readline
    N, M, Q = map(int, input().split())

    inf = 1 << 60
    dist = [[inf] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)
        dist[b][a] = min(dist[b][a], c)
    for i in range(1, N + 1):
        dist[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    ans = [0] * Q
    for i in range(Q):
        a, b = map(int, input().split())
        ans[i] = -1 if dist[a][b] == inf else dist[a][b]
    print("\n".join(map(str, ans)))


solve()
