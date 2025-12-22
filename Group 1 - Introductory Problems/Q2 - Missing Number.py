# https://cses.fi/problemset/task/1083
# Simple math, 3p
#
# We know the sum of the first n natural numbers, use the formula and subtract to get the missing number
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

print(n * (n + 1) // 2 - sum(arr))
