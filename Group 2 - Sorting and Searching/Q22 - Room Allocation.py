# https://cses.fi/problemset/task/1164
# Data structures + intervals (1D line sweep), 10p
#
# Simulate with line sweep, use existing room if possible, otherwise allocate a new one
# TC: O(nlogn)

import sys


def solve():
    input = sys.stdin.readline
    n = int(input())

    events = []
    for i in range(n):
        l, r = map(int, input().split())
        events.append((l, i, 1))
        events.append((r + 0.5, i, -1))
    events.sort(key=lambda x: x[0])

    rooms = 0
    available = []  # available room numbers
    allocation = [-1] * n
    for loc, i, diff in events:
        if diff == 1:  # need a room
            if not available:
                rooms += 1
                allocation[i] = rooms
            else:
                allocation[i] = available.pop()
        else:  # leaving a room
            available.append(allocation[i])

    print(rooms)
    print(" ".join(map(str, allocation)))


solve()
