# https://cses.fi/problemset/task/2220
# Digit DP, 12p
#
# Build number digit by digit
# dp[upper bounded?][leading zero?][idx][last digit] = number of ways of having this state as a prefix
# - upper bounded ensures that our states never exceed n
# - leading zeros ensures we don't look for duplicates until the number actually starts
#
# It's all constant factors so we don't look at TC
# Operations: 2 * 2 * 2 * 18 * 10 * 10 = 14400
# Note that we choose to do this recursively for clarity, and it skips some useless states


def count_no_adj(n):  # solves for [0, n]
    if n < 0:
        return 0

    s = list(map(int, str(n)))
    le = len(s)
    dp = [[[[-1] * 10 for _ in range(le + 1)] for _ in range(2)] for _ in range(2)]

    def solve(upper, zero, idx, prev):
        if idx == le:
            return 1
        if dp[upper][zero][idx][prev] != -1:
            return dp[upper][zero][idx][prev]
        total = 0
        mx = s[idx] if upper else 9
        for d in range(mx + 1):
            if d != prev or zero:
                total += solve(upper and s[idx] == d,
                               zero and d == 0,
                               idx + 1,
                               d)
        dp[upper][zero][idx][prev] = total
        return total

    return solve(True, True, 0, 0)


l, r = map(int, input().split())
print(count_no_adj(r) - count_no_adj(l - 1))
