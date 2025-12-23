# https://cses.fi/problemset/task/1092
# Greedy algorithms + simple math, 5p
#
# Knapsack-like problem, since we must take all, if one set has half, the other automatically does as well
# Since we get all numbers from 1 to n, simply use greedy
#
# TC: O(n)

import sys

n = int(input())

total = n * (n + 1) // 2
if total % 2 == 1:  # can't split into equal halves
    print("NO")
    sys.exit()

target = total // 2

set1 = []
set2 = []
cur = 0
for i in reversed(range(1, n + 1)):
    if cur + i <= target:
        cur += i
        set1.append(i)
    else:
        set2.append(i)

print("YES")
print(len(set1))
print(" ".join(map(str, set1)))
print(len(set2))
print(" ".join(map(str, set2)))
