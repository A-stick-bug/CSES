# https://cses.fi/problemset/task/1634
# Unbounded knapsack DP, 7p
#
# dp[x] = minimum number of coins to make a sum of x
# TC: O(n * X)

def solve():
    inf = 1 << 30

    n, X = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [inf] * (X + 1)
    dp[0] = 0
    for coin in arr:
        for i in range(coin, X + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    print(dp[X] if dp[X] != inf else -1)


solve()
