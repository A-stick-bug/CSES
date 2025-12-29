# https://cses.fi/problemset/task/1085
# Binary search, 10p
#
# Monotonicity:
# - if we can split into k subarrays with max sum X, we can also split into K+1 subarrays
# - clearly, we can binary search for X (if X works, X+1 also works)
#
# TC: O(nlogn)

# check if everything can fit into at most k groups, each with sum <= x
def works(x):
    groups = 1  # number of groups needed
    cur = 0  # current group size
    for i in arr:
        if cur + i > x:  # new group
            cur = i
            groups += 1
        else:
            cur += i
    return groups <= k


n, k = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)
ans = high
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        high = mid - 1
        ans = mid
    else:
        low = mid + 1

print(ans)
