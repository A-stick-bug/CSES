# https://cses.fi/problemset/task/1074
# Ad hoc + math, 7p
#
# It is optimal to turn every number into the median
# Intuition:
# - If we are not at the median, it is always better to move towards it since we are decreasing
#   the distance to more numbers than we are increasing
# - Notice that if n is even, any number between the two center numbers (inclusive) will work
#
# TC: O(nlogn)

n = int(input())
arr = list(map(int, input().split()))

median = sorted(arr)[len(arr) // 2]
print(sum(abs(i - median) for i in arr))
