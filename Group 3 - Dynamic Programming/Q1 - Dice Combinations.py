# https://cses.fi/problemset/task/1633
# Sequence DP, 7p
#
# Note that order matters here, so 1+2 is distinct from 2+1
# dp[x] = number of ways to make a sum of x using 1-6
# TC: O(n)

MOD = 10 ** 9 + 7
n = int(input())

dp = [0] * (n + 1)
dp[0] = 1  # 1 way to have nothing
for i in range(1, n + 1):
    # consider transitioning from previous state by adding a number from 1 to 6
    dp[i] = sum(dp[max(0, i - 6): i]) % MOD

print(dp[n])
