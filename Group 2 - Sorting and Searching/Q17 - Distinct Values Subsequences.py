# https://cses.fi/problemset/task/3421
# Combinatorics, 7p
#
# The answer is entirely dependent on the frequency of the values
# - we compute the frequencies with sorting to avoid hashing (dict)
#
# Independently consider each number x, with frequency f(x):
# - we have f(x)+1 choices, either don't take x or pick an x out of the f(x) options
#
# TC: O(nlogn)

MOD = 10 ** 9 + 7
n = int(input())
arr = sorted(map(int, input().split()))

freq = [1]  # frequency list, values only
for i in range(1, n):
    if arr[i] != arr[i - 1]:
        freq.append(1)
    else:
        freq[-1] += 1

total = 1
for f in freq:
    total *= f + 1
    total %= MOD

print((total - 1) % MOD)  # exclude empty list
