# https://cses.fi/problemset/task/1621
# Sorting, 5p
#
# Note: using a set works, but since the category is sorting, we'll do that instead
# TC: O(nlogn)

n = int(input())
arr = sorted(map(int, input().split()))

total = 1
for i in range(1, n):
    if arr[i] != arr[i - 1]:
        total += 1
print(total)
