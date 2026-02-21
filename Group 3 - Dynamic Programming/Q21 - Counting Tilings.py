# https://cses.fi/problemset/task/2181
# Bitmask/grid dp, 15p
#
# We use bitmask to track the axis with dimension n<=10
# dp[col][mask] = number of ways
#
# To avoid overlap, the states represent the number of ways of having the first `col` columns filled
# and the newest column having state `mask`. The set bits in `mask` represent tiles that extend from
# the previous column, thus 2 adjacent set bits will never represent a vertically tiled domino in the
# current column.
#
# TC: O(m * 2^n * T(n)), where T(n) is the number of transitions per state
# T(n) has upper bound fib(n) ~ 1.6^n, but is much better on average
#
# Improvements to TC bound:
# By looking at how the total number of transitions scale with n, I found the following
# - https://oeis.org/A000129
# This gives us an accurate time complexity: O(m * P(n)), where P(n) is the n-th Pell number
# Asymptotically, it is around O(m * 2.4^n), using this, we get a transition cost of around 1.2^n per state
#
# Or just say O(m * 2^n) and call it a day since n is <=10 anyway

def transitions(mask):  # generate transitions to next column's state from mask
    res = []

    def generate(cur, i):
        if i == n:
            res.append(cur)
            return
        if mask & (1 << i):  # already filled, do nothing
            generate(cur, i + 1)
        else:
            generate(cur | (1 << i), i + 1)  # horizontal, extend to next
            if i != n - 1 and not mask & (1 << (i + 1)):  # vertical
                generate(cur, i + 2)

    generate(0, 0)
    return res


n, m = map(int, input().split())

dp = [[0] * (1 << n) for _ in range(m + 1)]
FULL = (1 << n) - 1
MOD = 10 ** 9 + 7

push = [[] for _ in range(1 << n)]  # transitions from i to push[i]
for mask in range(1 << n):
    push[mask] = transitions(mask)

dp[0][0] = 1  # base case: have nothing
for i in range(m):
    for mask in range(1 << n):  # transition to next column
        dp[i][mask] %= MOD
        for nxt in push[mask]:
            dp[i + 1][nxt] += dp[i][mask]

print(dp[-1][0] % MOD)
