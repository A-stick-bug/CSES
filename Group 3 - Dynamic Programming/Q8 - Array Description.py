# https://cses.fi/problemset/task/1746
# Sequence DP, 10p
#
# dp[i][x] = number of ways of having first `i` numbers, with the rightmost being `x`
# TC: O(nm)

def solve():
    MOD = 10 ** 9 + 7
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [0] * (m + 2)
    if arr[0] == 0:
        for x in range(1, m + 1):  # base cases, no restrictions at first
            dp[x] = 1
    else:
        dp[arr[0]] = 1  # base cases, only 1 option

    for i in range(1, n):
        if arr[i] != 0:  # restrict
            keep = dp[arr[i] - 1] + dp[arr[i]] + dp[arr[i] + 1]
            dp = [0] * (m + 2)
            dp[arr[i]] = keep
        else:
            new_dp = [0] * (m + 2)
            for x in range(1, m + 1):
                new_dp[x] = (dp[x - 1] + dp[x] + dp[x + 1]) % MOD
            dp = new_dp

    print(sum(dp) % MOD)


solve()
