# https://cses.fi/problemset/task/2217
# Ad hoc, 10p
#
# Our answer is entirely dependent on how many indices have loc[i]<loc[i-1]
# After swapping (a,b), we updated their locations, so we need to reevaluate the surrounding values
# Essentially, we are maintaining the number of moves, and updating after every swap in O(1)
#
# For Python magic reasons, we wrap the entire code in a function to avoid overhead from global variables
# This is necessary to not TLE (I used CPython)
# TC: O(n + m)

import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [n + 1]  # padding

    loc = [-1] * (n + 2)
    for i in range(n + 2):
        loc[arr[i]] = i

    moves = 1 + sum(loc[i] < loc[i - 1] for i in range(2, n + 1))

    def get_cost(a, b):  # get the cost incurred by numbers a,b (not indices)
        if a > b:
            a, b = b, a
        cost = loc[a] < loc[a - 1]
        cost += loc[b + 1] < loc[b]
        cost += loc[b] < loc[b - 1]
        if a + 1 != b:  # avoid overcount if they are adjacent
            cost += loc[a + 1] < loc[a]
        return cost

    ans = [0] * m
    for case in range(m):
        a, b = map(int, input().split())
        num1, num2 = arr[a], arr[b]

        # update values around a and b
        old = get_cost(num1, num2)
        loc[num1], loc[num2] = loc[num2], loc[num1]
        arr[a], arr[b] = arr[b], arr[a]
        new = get_cost(num1, num2)

        moves -= old
        moves += new

        ans[case] = moves

    print("\n".join(map(str, ans)))


solve()
