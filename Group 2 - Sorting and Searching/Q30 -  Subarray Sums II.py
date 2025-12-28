# https://cses.fi/problemset/task/1661
# Prefix sums, 7p
#
# We use the prefix sum of arr for efficient subarray sums
# Similar to in 2-SUM, we use a dict to find matching values that sum to X
#
# TC: O(n)

from itertools import accumulate
from random import randint
from collections import defaultdict

XOR = randint(1, 10 ** 18)

n, X = map(int, input().split())
arr = list(map(int, input().split()))

psa = [0] + list(accumulate(arr))

total = 0
prev = defaultdict(int)  # previous prefix values
for i in range(n + 1):
    target = psa[i] - X
    if target ^ XOR in prev:
        total += prev[target ^ XOR]
    prev[psa[i] ^ XOR] += 1

print(total)
