# https://cses.fi/problemset/task/1192
# Flood fill/DFS, 7p
# Once we encounter an open region, fill it with walls entirely so we don't overcount
#
# TC: O(RC)

def flood_fill(r, c):
    grid[r][c] = "#"
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == ".":
                grid[nr][nc] = "#"
                stack.append((nr, nc))


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

total = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == ".":
            total += 1
            flood_fill(r, c)
print(total)
