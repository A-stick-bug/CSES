# https://cses.fi/problemset/task/1094
# Implementation + simple math, 3p
#
# Simulate from left to right, making each element as least as large as the previous
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        total += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]

print(total)
