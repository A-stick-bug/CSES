# https://cses.fi/problemset/task/1071
# High school math, 5-7p
#
# The diagonal is given by f(n) = n^2 - n + 1
# Depending on parity, we adjust the answer based on how far we are from the diagonal
#
# TC: O(1) per test case

import sys

input = sys.stdin.readline


def solve():
    r, c = map(int, input().split())

    ring = max(r, c)  # the layer of the 'ring' that (r,c) is on
    center = ring ** 2 - ring + 1
    if ring % 2 == 0:
        if c >= r:
            print(center - (c - r))
        else:
            print(center + (r - c))
    else:
        if c >= r:
            print(center + (c - r))
        else:
            print(center - (r - c))


t = int(input())
for _ in range(t):
    solve()
