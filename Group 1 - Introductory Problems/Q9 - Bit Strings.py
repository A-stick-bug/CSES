# https://cses.fi/problemset/task/1617
# Simple math, 3-5p, depending on familiarity with basic modular arithmetic
# Binary exponentiation would be ~10p, but you can just use a for loop since n <= 10^6
#
# 2 choices for each index, so answer is just 2^n
# TC: O(log(n)) by binary exponentiation

n = int(input())
print(pow(2, n, 10 ** 9 + 7))
