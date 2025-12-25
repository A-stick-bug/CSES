# https://cses.fi/problemset/task/2183
# Math, 7p
#
# Loop small to large and track the numbers that are possible
# - If the new number is >sum+1, then we can't form `sum+1` since everything smaller
#   is not enough and everything bigger is too big
#
# TC: O(nlogn)

import sys

n = int(input())
arr = sorted(map(int, input().split()))

possible = 0  # max number possible so far
for val in arr:
    if val > possible + 1:
        print(possible + 1)
        sys.exit()
    else:  # extend set of possible values
        possible += val

print(possible + 1)
