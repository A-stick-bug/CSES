# https://cses.fi/problemset/task/1630
# Greedy algorithms, 7p
#
# We simplify the math, pretend the reward for a task is -f where f is when you finish
# We can do this since the +d is constant no matter what order we take
# Intuitively, we want to finish the shorter tasks first to reduce penalty per unit of time
#
# TC: O(nlogn)

import sys

input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])  # sort by length of task

total = 0
cur_time = 0
for t, deadline in arr:
    cur_time += t
    total += deadline - cur_time

print(total)
