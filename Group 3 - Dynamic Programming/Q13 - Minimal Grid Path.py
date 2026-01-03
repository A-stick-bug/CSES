# TLE IN PYTHON
#
# https://cses.fi/problemset/task/3359
# Greedy + BFS, 10-12p
#
# Since we are looking for lex min, always prioritize early characters -> greedy
# If there is a tie, we maintain all indices that create optimal strings
#
# TC: O(n^2)

n = int(input())
grid = [input() for _ in range(n)]

vis = [[False] * n for _ in range(n)]
res = []
q1 = [0]  # parallel list to avoid tuples
q2 = [0]
for le in range(1, 2 * n):  # layer by layer BFS
    # only keep optimal (and tied) characters
    min_char = min(grid[r][c] for r, c in zip(q1, q2))
    res.append(min_char)
    keep_idx = [i for i in range(len(q1)) if grid[q1[i]][q2[i]] == min_char]
    q1 = [q1[i] for i in keep_idx]
    q2 = [q2[i] for i in keep_idx]

    nxt1 = []
    nxt2 = []
    for r, c in zip(q1, q2):  # consider next characters
        if r + 1 < n and not vis[r + 1][c]:
            vis[r + 1][c] = True
            nxt1.append(r + 1)
            nxt2.append(c)
        if c + 1 < n and not vis[r][c + 1]:
            vis[r][c + 1] = True
            nxt1.append(r)
            nxt2.append(c + 1)

    q1 = nxt1
    q2 = nxt2

print("".join(res))

# # scrapped idea, this is overkill as it solves for all possible starting points
# Grid DP + reconstruction, 12-15p
#
# Consider the strings formed by starting at (r,c) and going to the end
# We only need to track the relative lexicographical order of strings of the same length
#
# dp[r][c] = relative lex order of string starting at (r,c) compared to equal length strings
# We do the transitions from small to large length (i.e. 1 diagonal at a time)
# When doing transitions, prioritize the early letter, tiebreak by rest of the string
#
# TC: O(n^2 * log(n))
