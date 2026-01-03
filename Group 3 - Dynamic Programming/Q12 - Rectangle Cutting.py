# https://cses.fi/problemset/task/1744
# 2D sequence DP? (looks like interval DP too), 10p
#
# dp[i][j] = minimum number of moves to make i by j rectangle
# We can use symmetry to reduce 2x constant factors
#
# TC: O(n * m * (n+m))

n, m = map(int, input().split())

inf = 1 << 30
dp = [[inf] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == j:  # base case: square
            dp[i][j] = 0
            continue
        if j < i and j <= n and i <= m:  # symmetry
            dp[i][j] = dp[j][i]
            continue

        # try all possible splits, up to half by symmetry
        if i > 1:
            dp[i][j] = min(dp[i][j], min(1 + dp[split1][j] + dp[i - split1][j] for split1 in range(1, i // 2 + 1)))
        if j > 1:
            dp[i][j] = min(dp[i][j], min(1 + dp[i][split2] + dp[i][j - split2] for split2 in range(1, j // 2 + 1)))

print(dp[n][m])
