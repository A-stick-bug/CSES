# https://cses.fi/problemset/task/1093
# Knapsack DP + modular arithmetic, 10p
#
# dp[x] = number of ways to get a sum of x
# TC: O(n^3)

import sys

MOD = 10 ** 9 + 7
mod_div = lambda p, r: (p * pow(r, MOD - 2, MOD)) % MOD

n = int(input())

total = n * (n + 1) // 2
if total % 2 == 1:  # can't split evenly
    print(0)
    sys.exit()

target = total // 2

dp = [0] * (target + 1)
dp[0] = 1
for val in range(1, n + 1):
    for i in reversed(range(val, target + 1)):
        dp[i] += dp[i - val]
        dp[i] %= MOD

print(mod_div(dp[target], 2))  # symmetry, divide by 2 but use modular arithmetic
