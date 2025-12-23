# https://cses.fi/problemset/task/1622
# Recursion, 7p
#
# Generate all non-duplicate permutations of a string in alphabetical order
# We avoid generating all n! permutations and removing duplicates
# Instead, insert each group of characters with combinations
#
# TC: O(n * n!)

from collections import Counter
from itertools import combinations


def combine(f, sub):
    char, cnt = f
    res = []
    for cur in sub:
        new_le = len(cur) + cnt
        for comb in combinations(list(range(new_le)), cnt):
            new = [None] * new_le
            for idx in comb:
                new[idx] = char
            other = 0
            for i in range(new_le):
                if not new[i]:
                    new[i] = cur[other]
                    other += 1
            res.append(new)
    return res


def generate(freq):
    if len(freq) == 1:
        char, cnt = freq[0]
        return [[char] * cnt]
    sub = generate(freq[1:])
    return combine(freq[0], sub)


s = input()
n = len(s)

freq = sorted(Counter(s).items())
res = generate(freq)

res.sort()
print(len(res))
for i in res:
    print("".join(i))
