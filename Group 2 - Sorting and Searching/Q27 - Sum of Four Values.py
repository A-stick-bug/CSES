# https://cses.fi/problemset/task/1642
# Solution 1: Use the 3-SUM code with an extra for loop, 7p, O(n^3)
#
# Solution 2: Stores pairs in a dict and match (basically 2-SUM but in pairs), 10p, O(n^2)
#
# Note: solution 2 is not strictly better since dict can be hacked and the constant factor is high


# solution 1
def solve():
    n, X = map(int, input().split())
    arr = list(map(int, input().split()))  # arr and idx are parallel lists, avoid tuples for speed
    idx = sorted(range(n), key=lambda i: arr[i])
    arr.sort()

    for h in range(n - 3):
        for i in range(h + 1, n - 2):  # try all `i`
            k = n - 1
            target = X - arr[i] - arr[h]
            for j in range(i + 1, n - 1):  # 2-pointers on j,k
                while k > j and arr[j] + arr[k] > target:
                    k -= 1
                if k == j:
                    break
                if arr[j] + arr[k] == target:
                    print(idx[i] + 1, idx[j] + 1, idx[k] + 1, idx[h] + 1)
                    return

    print("IMPOSSIBLE")


solve()

# # Solution 2
# # NOTE: this is not completely correct, I did a temporary fix with randomization
# import sys
# from collections import defaultdict
# from random import randint, shuffle
#
# XOR = randint(1, 10 ** 18)  # shuffle the keys to hopefully make it harder to hack
#
# n, X = map(int, input().split())
# arr = list(map(int, input().split()))
#
# mp = defaultdict(list)
# for i in range(n):
#     for j in range(i + 1, n):
#         mp[(arr[i] + arr[j]) ^ XOR].append((i, j))
#
# for k in mp:  # :)
#     shuffle(mp[k])
#
# for k in mp:
#     for i, j in mp[k][:10]:  # take a few, hopefully no overlap
#         target = X - (k ^ XOR)
#         if XOR ^ target not in mp:
#             continue
#         for a, b in mp[XOR ^ target][:10]:
#             if len({a, b, i, j}) == 4:  # hopefully no overlap
#                 print(a + 1, b + 1, i + 1, j + 1)
#                 sys.exit()
#
# print("IMPOSSIBLE")
