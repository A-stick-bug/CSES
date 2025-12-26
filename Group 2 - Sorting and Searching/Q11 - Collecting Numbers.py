# https://cses.fi/problemset/task/2216
# Ad hoc, 5-7p
#
# The key idea is tracking the locations of each number
# Lopping from 1 to n, if we ever have to move left, we know it will take another walk
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

loc = [-1] * (n + 1)
for i in range(n):
    loc[arr[i]] = i

total = 0
prev = n + 2
for i in range(1, n + 1):
    if loc[i] < prev:
        total += 1
    prev = loc[i]

print(total)
