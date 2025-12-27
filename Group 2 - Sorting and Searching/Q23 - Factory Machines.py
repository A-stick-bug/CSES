# https://cses.fi/problemset/task/1620
# Binary search + simple math, 5-7p
#
# Binary search for `t`, check in O(n) if a given value works
# TC: O(n * log(MX)), MX~10^18

n, t = map(int, input().split())
arr = list(map(int, input().split()))


def works(k):  # check if `k` seconds is enough to make `t` products
    return sum(k // unit for unit in arr) >= t


low = 0
high = 10 ** 18 + 1
ans = high
while low <= high:
    mid = (low + high) // 2
    if works(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)
