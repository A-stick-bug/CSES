# https://cses.fi/problemset/task/1755
# Implementation, 5p
#
# Notice that at most 1 character can have an odd frequency (goes in the middle)
# TC: O(n)

import sys
from collections import Counter

s = input()
n = len(s)

freq = Counter(s)

if sum(i % 2 == 1 for i in freq.values()) > 1:  # more than 1 odd
    print("NO SOLUTION")
    sys.exit()

res = []
odd = None
for char, cnt in freq.items():
    res.extend(char * (cnt // 2))
    if cnt % 2 == 1:
        odd = char

if odd:
    res = res + [odd] + res[::-1]
else:
    res = res + res[::-1]
print("".join(res))
