# https://cses.fi/problemset/task/1145
# LIS DP, 10-12p
# This is the standard longest increasing subsequence problem
#
# Let dp[x] = the minimum ending value of a LIS with length x (1-index)
#
# Note: Another way is dp + segment tree
#
# TC: O(nlogn)

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = []  # base case: first element
for val in arr:
    idx = bisect_left(dp, val)
    if idx == len(dp):
        dp.append(val)
    else:
        dp[idx] = val

print(len(dp))
