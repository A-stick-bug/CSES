# https://cses.fi/problemset/task/1638
# Grid DP (2D sequence DP), 7p
#
# dp[r][c]: number of ways to get to (r,c)
# TC: O(n^2)

MOD = 10 ** 9 + 7
n = int(input())
grid = [input() for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]  # 1-index for padding
dp[1][1] = 1 if grid[0][0] != "*" else 0

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if r == c == 1:
            continue
        if grid[r - 1][c - 1] == "*":
            continue
        dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % MOD

print(dp[n][n])
