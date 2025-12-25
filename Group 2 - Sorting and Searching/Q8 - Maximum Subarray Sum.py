# https://cses.fi/problemset/task/1643
# Prefix sums, 5-7p
#
# Kadane's algorithm can be unintuitive, instead we think in prefix sums
# A subarray is a prefix minus a smaller prefix
# Max subarray sum = max(pref[r] - pref[l])
# - we can maintain the minimum of the prefix sum to the left and subtract it
#
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

best = max(arr)
pref_min = 0
pref = 0
for i in arr:
    pref += i
    best = max(best, pref - pref_min)
    pref_min = min(pref, pref_min)

print(best)
