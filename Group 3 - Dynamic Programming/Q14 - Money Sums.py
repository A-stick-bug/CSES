# https://cses.fi/problemset/task/1745
# Knapsack DP, 7p
#
# dp[x] = whether a sum of x is achievable
# Since Python is slow, we use bitmask to speed it up (10p difficulty)
#
# TC: O(n * sum(arr))

n = int(input())
arr = list(map(int, input().split()))

dp = 1
for val in arr:
    dp |= dp << val

s = bin(dp)[2:]
res = [i for i in range(1, sum(arr) + 1) if s[i] == "1"]

print(dp.bit_count() - 1)
print(" ".join(map(str, res)))
