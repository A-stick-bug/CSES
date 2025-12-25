# https://cses.fi/problemset/task/1640
# 2-pointers, 7p
#
# This is the classic 2-sum problem
# Note that we avoid hashing (dict) for now since they are easy to hack
# TC: O(nlogn)

import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(arr[i], i) for i in range(n)]
arr.sort(key=lambda x: x[0])

j = n - 1
for i in range(n):
    while j > i and arr[i][0] + arr[j][0] > k:
        j -= 1
    if j > i and arr[i][0] + arr[j][0] == k:
        print(arr[i][1] + 1, arr[j][1] + 1)
        sys.exit()

print("IMPOSSIBLE")
