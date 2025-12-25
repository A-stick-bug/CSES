# https://cses.fi/problemset/task/1619
# Line sweep/difference array, 7p
#
# Sort start and end events by time and process left to right
# TC: O(nlogn)

import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

events = []
for l, r in arr:
    events.append((l, 1))
    events.append((r, -1))
events.sort(key=lambda x: x[0])

mx = 0
cur = 0
for t, diff in events:
    cur += diff
    mx = max(mx, cur)
print(mx)
