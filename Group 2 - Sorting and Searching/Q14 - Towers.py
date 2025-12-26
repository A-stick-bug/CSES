# https://cses.fi/problemset/task/1073
# Greedy, 10p
# Simple code, complex justification
#
# Strategy:
# If possible, put the current cube onto the tower with the smallest possible top cube, to save space for future cubes
# - it is slightly harder to see why you wouldn't start a new tower here
# Otherwise, start a new tower
# Notice how this preserves monotonicity of `towers` and cleanly allows for binary search
#
# TC: O(nlogn)

from bisect import bisect_right

n = int(input())
arr = list(map(int, input().split()))

# track the top (smallest) cube in each existing tower
# this is always monotonic increasing
towers = []
for i in arr:
    idx = bisect_right(towers, i)
    if idx >= len(towers):  # new tower needed
        towers.append(i)
    else:
        # sketch of monotonicity proof:
        # - in order to break monotonicity, we must have that towers[idx-1] > towers[idx]
        # - however, this cannot happen as otherwise we would've simply put the cube onto idx-1
        #  - i.e. contradicts the bisect_right
        towers[idx] = i

print(len(towers))
