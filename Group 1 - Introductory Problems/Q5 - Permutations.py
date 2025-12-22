# https://cses.fi/problemset/task/1070
# Constructive + simple math, 5p
#
# Construction:
# - space adjacent numbers 1 index apart
# - e.g. 1 5 2 6 3 7 4 8
# This doesn't work for n < 5 so we handle those as edge cases
#
# TC: O(n)

n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
elif n == 4:
    print("2 4 1 3")
else:
    ans = []
    half = (n + 1) // 2
    for i in range(1, half + 1):
        ans.append(i)
        ans.append(i + half)
    if n % 2 == 1:  # odd case: extra number
        ans.pop()

    print(" ".join(map(str, ans)))
