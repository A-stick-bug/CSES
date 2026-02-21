# https://cses.fi/problemset/task/1193
# BFS shortest path + path reconstruction, 10p
#
# For convenience, we directly mark our path on the given grid
# Once we arrive at B, trace the path back to A
#
# TC: O(RC)

import sys
from collections import deque

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

move = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}
start = None
for r in range(R):
    for c in range(C):
        if grid[r][c] == "A":
            start = (r, c)

prev = [[None] * C for _ in range(R)]  # track previous location
q = deque([start])
while q:
    r, c = q.popleft()

    for mv, (dr, dc) in move.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if grid[nr][nc] == "B":  # trace path back to A
                moves = [mv]
                rr, cc = r, c
                while prev[rr][cc]:
                    moves.append(grid[rr][cc])
                    rr, cc = prev[rr][cc]
                moves.reverse()
                print("YES")
                print(len(moves))
                print("".join(moves))
                sys.exit()
            elif grid[nr][nc] == ".":
                grid[nr][nc] = mv
                q.append((nr, nc))
                prev[nr][nc] = (r, c)

print("NO")
