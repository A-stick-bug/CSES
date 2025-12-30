# https://cses.fi/problemset/task/1637
# Sequence DP or greedy algorithms, 7p
#
# dp[x] = minimum number of steps to get from x to 0
# TC: O(n)

inf = 1 << 30
n = int(input())

dp = [inf] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    digits = set(map(int, str(i)))
    for d in digits:
        if i - d >= 0:
            dp[i] = min(dp[i], dp[i - d] + 1)

print(dp[n])
