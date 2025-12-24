# https://cses.fi/problemset/task/3217
# Graph theory, 7p
#
# Template BFS on a grid, nothing to say here
# TC: O(n^2)

from collections import deque

n = int(input())

knight_dir = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
dist = [[-1] * n for _ in range(n)]
dist[0][0] = 0
q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    for dr, dc in knight_dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

for row in dist:
    print(*row)
