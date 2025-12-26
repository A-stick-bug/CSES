# https://cses.fi/problemset/task/2162
# Implementation + simple math, 5-7p
#
# We can simulate the removal directly since every run through the array cuts the length in half
# n + n/2 + n/4 + n/8 + ... is around 2n
# TC: O(n)

n = int(input())

arr = list(range(1, n + 1))

removed = []
start_idx = 0  # index that we start removing at, either 0 or 1
while arr:
    flip = len(arr) % 2  # if length is odd, we need to change the starting index next run
    removed.extend(arr[start_idx ^ 1::2])  # ^1 changes start_idx between 0 and 1
    arr = arr[start_idx::2]
    if flip:
        start_idx ^= 1

print(" ".join(map(str, removed)))
