# https://cses.fi/problemset/task/1662
# Prefix sums + basic modular arithmetic, 10p
#
# Divisible by n <=> remainder is 0
# Track the remainders of prefix sums
# Key fact: If psa[r] and psa[l] both have remainder x, then psa[r]-psa[l] has remainder 0
#
# TC: O(n)

n = int(input())
arr = list(map(int, input().split()))

total = 0
acc = 0  # current prefix sum
prev = [0] * n  # number of previous prefixes with remainder `x` (mod n)
prev[0] += 1  # empty prefix
for i in range(n):
    acc += arr[i]
    acc %= n
    total += prev[acc]  # match with same remainders
    prev[acc] += 1

print(total)
