# https://cses.fi/problemset/task/1754
# Ad hoc, 5p
#
# Each move removes 3 coins, we can figure out how many moves we make
# Consider if we can apply -1 enough times
#
# TC: O(1) per test case

import sys

input = sys.stdin.readline


def solve():
    a, b = map(int, input().split())
    if (a + b) % 3 != 0:
        print("NO")
        return

    moves = (a + b) // 3

    if a < moves or b < moves:  # can't apply -1 enough times
        print("NO")
        return

    print("YES")


t = int(input())
for _ in range(t):
    solve()
