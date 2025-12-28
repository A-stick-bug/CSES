# https://cses.fi/problemset/task/1645
# Monotonic stack, 10p
#
# Note that we could maintain some log(n) data structure of previous indices but this is much simpler
# The idea is that once we are at index i, we can ignore previous indices with bigger values since they can
# never be the nearest smaller value anymore (index i has both a smaller value and is closer to future indices)
#
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n
stack = []
for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] + 1  # 1-index answer
    stack.append(i)

print(" ".join(map(str, ans)))
