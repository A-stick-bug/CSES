# https://cses.fi/problemset/task/2431
# Simple math, 5-7p
#
# We group the digits by 'size of group' and find the group that `k` is in
# - i.e. [1-9][10-99][100-999][etc.]
# The group sizes are 9, 90, 900, etc.
#
# TC: O(log(k)) per query

def solve():
    k = int(input())
    k -= 1  # 0-index

    acc = 0
    for group in range(1, 20):
        sz = group * 9 * (10 ** (group - 1))
        if acc + sz >= k:  # found group
            k -= acc
            idx = k // group  # get number within group
            pos = k % group  # get position within number
            num = str(10 ** (group - 1) + idx)
            print(num[pos])
            break
        acc += sz


t = int(input())
for _ in range(t):
    solve()
