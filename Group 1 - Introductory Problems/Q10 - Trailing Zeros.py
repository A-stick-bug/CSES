# https://cses.fi/problemset/task/1618
# Number theory, 7-10p
#
# Basic application of Legendre's formula: https://en.wikipedia.org/wiki/Legendre%27s_formula
# TC: O(log(n))

def highest_power(n, p):  # highest power of p that divides n!
    total = 0
    cur = p
    while cur <= n:
        total += n // cur
        cur *= p
    return total


n = int(input())
print(min(highest_power(n, 2), highest_power(n, 5)))
# technically we only need the highest power of 5 since there are always more powers of 2
