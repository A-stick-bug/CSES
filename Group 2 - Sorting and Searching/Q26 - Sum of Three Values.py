# https://cses.fi/problemset/task/1641
# 2-pointers, 7p
#
# This is the classic 3-SUM problem
# TC: O(n^2)

def solve():
    n, X = map(int, input().split())
    arr = list(map(int, input().split()))  # arr and idx are parallel lists, avoid tuples for speed
    idx = sorted(range(n), key=lambda i: arr[i])
    arr.sort()

    for i in range(n - 2):  # try all `i`
        k = n - 1
        target = X - arr[i]
        for j in range(i + 1, n - 1):  # 2-pointers on j,k
            while k > j and arr[j] + arr[k] > target:
                k -= 1
            if k == j:
                break
            if arr[j] + arr[k] == target:
                print(idx[i] + 1, idx[j] + 1, idx[k] + 1)
                return

    print("IMPOSSIBLE")


solve()
