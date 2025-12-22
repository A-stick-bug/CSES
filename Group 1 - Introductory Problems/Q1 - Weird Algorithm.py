# https://cses.fi/problemset/task/1068
# Implementation, 3p
#
# Simulate the Collatz conjecture
# TC: unknown, takes at most 525 steps for n <= 10^6

n = int(input())

res = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2
        res.append(n)
    else:
        n = 3 * n + 1
        res.append(n)

print(" ".join(map(str, res)))
