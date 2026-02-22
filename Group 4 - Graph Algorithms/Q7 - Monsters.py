# https://cses.fi/problemset/task/1194
# Multi-source BFS + path reconstruction, 10p
#
# Precompute the earliest time that monsters reach each cell with multi source bfs
# Then run normal bfs with the player, ensuring we never go to a cell possibly occupied by a monster
#
# TC: O(n + m)

import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

inf = 1 << 30
move = [('D', 1, 0), ('U', -1, 0), ('L', 0, -1), ('R', 0, 1)]
monsters = deque()
player = deque()
vis = [[inf] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if grid[i][j] == "M":
            monsters.append((i, j))
            vis[i][j] = 0
        elif grid[i][j] == "A":
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                print("YES")
                print(0)
                sys.exit()
            player.append((0, i, j))

while monsters:
    r, c = monsters.popleft()
    for _, dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#" and vis[nr][nc] == inf:
            vis[nr][nc] = vis[r][c] + 1
            monsters.append((nr, nc))

prev = [[None] * C for _ in range(R)]
while player:
    t, r, c = player.popleft()
    for mv, dr, dc in move:
        nr, nc = r + dr, c + dc

        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "." and vis[nr][nc] > t + 1:
            if nr == 0 or nr == R - 1 or nc == 0 or nc == C - 1:  # finish
                moves = [mv]
                rr, cc = r, c
                while prev[rr][cc]:
                    moves.append(prev[rr][cc][2])
                    rr, cc, _ = prev[rr][cc]
                moves.reverse()
                print("YES")
                print(len(moves))
                print("".join(moves))
                sys.exit()
            else:
                grid[nr][nc] = "!"  # mark visited
                player.append((t + 1, nr, nc))
                prev[nr][nc] = (r, c, mv)

print("NO")
