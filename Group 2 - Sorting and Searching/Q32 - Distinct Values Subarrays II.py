# https://cses.fi/problemset/task/2428
# Sliding window/2-pointers, 10p
#
# Similar to part 1 [G2 Q16 - Distinct Values Subarrays](https://cses.fi/problemset/task/3420)
# Again, solve for all endpoints `r`, the valid `l` are guaranteed to extend from some previous index to `r`
# TC: O(n)

from random import randint
from collections import defaultdict

XOR = randint(1, 10 ** 18)
n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
freq = defaultdict(int)
l = 0
for r in range(n):
    freq[arr[r] ^ XOR] += 1
    while len(freq) > k:
        freq[arr[l] ^ XOR] -= 1
        if freq[arr[l] ^ XOR] == 0:
            del freq[arr[l] ^ XOR]
        l += 1

    total += r - l + 1

print(total)
