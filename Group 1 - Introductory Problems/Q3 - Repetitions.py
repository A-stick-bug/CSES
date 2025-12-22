# https://cses.fi/problemset/task/1069
# Implementation, 5p
#
# Keep track of running sequence length and maximum
# TC: O(n)

s = input()
n = len(s)

cur = longest = 1
for i in range(1, n):
    if s[i] == s[i - 1]:
        cur += 1
    else:
        cur = 1
    longest = max(longest, cur)
print(longest)
