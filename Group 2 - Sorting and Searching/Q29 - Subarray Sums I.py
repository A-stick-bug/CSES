# https://cses.fi/problemset/task/1660
# Sliding window/2-pointers, 7p
#
# Since all values are positive, we try all possible endpoints r and adjust l accordingly
# Note: The solution in part 2 is also valid here and is not much harder
# TC: O(n)

n, X = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
l = 0
cur = 0  # current subarray sum
for r in range(n):
    cur += arr[r]
    while cur > X:
        cur -= arr[l]
        l += 1
    if cur == X:
        total += 1

print(total)
