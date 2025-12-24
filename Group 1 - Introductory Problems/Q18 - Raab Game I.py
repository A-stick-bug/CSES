# https://cses.fi/problemset/task/3399
# Game theory + constructive, 7-10p
#
# We consider extreme cases and notice that everything 'in-between' is possible
#
# TC: O(n) per test case

def solve():
    n, a, b = map(int, input().split())

    if a + b > n:  # can't have more wins than total games
        print("NO")
        return

    ties = n - a - b
    move1 = []  # moves for players
    move2 = []

    for i in range(1, ties + 1):
        move1.append(i)
        move2.append(i)

    if ties == n:  # edge case: all tied
        print("YES")
        print(" ".join(map(str, move1)))
        print(" ".join(map(str, move2)))
        return

    if a == 0 or b == 0:  # notice that one person winning results in at least 1 win for the other
        print("NO")
        return

    for i in range(a):
        move1.append(n - i)
        move2.append(n - i - b)
    for i in range(b):
        move1.append(n - i - a)
        move2.append(n - i)

    print("YES")
    print(" ".join(map(str, move1)))
    print(" ".join(map(str, move2)))


t = int(input())
for _ in range(t):
    solve()
