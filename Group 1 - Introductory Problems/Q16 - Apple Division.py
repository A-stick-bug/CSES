# https://cses.fi/problemset/task/1623
# Solution 1: recursion or bitmask, 7p, TC: O(n * 2^n)
#
# Solution 2: meet in the middle, 10-12p
# - Generate all possible left and right subsets
# - For each left subset, match with the best right subset efficiently
#
# TC: O(n * sqrt(2^n)) i.e. O(n * 2^(n/2))

# solution 2

def get_subset_sums(a):  # get all possible subset sums of `a`
    sums = []
    for mask in range(1 << len(a)):
        cur = 0
        for i in range(n):
            if mask & (1 << i):
                cur += a[i]
        sums.append(cur)
    return sums


n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

set1 = get_subset_sums(arr[:n // 2])
set2 = get_subset_sums(arr[n // 2:])
set1.sort()
set2.sort(reverse=True)
# print(set1, set2)

best = total
target = total / 2
idx2 = 0
for idx1 in range(len(set1)):
    while idx2 < len(set2) and set2[idx2] + set1[idx1] > target:
        idx2 += 1

    if idx2 + 1 < len(set2):
        cur2 = set1[idx1] + set2[idx2 + 1]
        best = min(best, abs((total - cur2) - cur2))

    if idx2 < len(set2):
        cur = set1[idx1] + set2[idx2]
        best = min(best, abs((total - cur) - cur))

print(best)

# # solution 1
# n = int(input())
# arr = list(map(int, input().split()))
#
# total = sum(arr)
# best = total
# for mask in range(1 << n):
#     cur = 0
#     for i in range(n):
#         if mask & (1 << i):
#             cur += arr[i]
#     best = min(best, abs((total - cur) - cur))
#
# print(best)
