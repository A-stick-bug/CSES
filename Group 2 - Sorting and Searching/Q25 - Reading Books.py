# https://cses.fi/problemset/task/1631
# Ad hoc, 7p
#
# Intuition: we can expect the answer to be sum(arr) most the time since we are
#            given full control on the order they read the books
# Looking at cases where you need more time:
# - longest book takes more than the rest -> other person must wait (answer is 2*max)
#
# In all other cases, we can create a construction with 0 wasted time
# - p1 will read the longest book first, then the other ones in order
# - p2 will read the other books in order, then the longest book last
# - it can be proven that there is no overlap
#
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

mx = max(arr)
print(max(2 * mx, sum(arr)))
