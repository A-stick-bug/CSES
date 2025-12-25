# https://cses.fi/problemset/task/1629
# Greedy, 7-10p
#
# This is the classic task scheduling problem
# Greedy strategy: watch the movie that ends earliest
# TC: O(nlogn)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])  # by end time

prev = -1  # previous ending time
total = 0
for l, r in arr:
    if l >= prev:
        prev = r
        total += 1

print(total)
