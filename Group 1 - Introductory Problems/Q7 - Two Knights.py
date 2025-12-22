# https://cses.fi/problemset/task/1072
# Solution 1: cheese, plug sample input into OEIS (https://oeis.org/A172132)
#
# Solution 2: analysis based, not implemented here
# - brute force the first few terms and find a pattern
#   - e.g. look at log-log plot, try polynomial regression
#
# Solution 3: mathematical derivation shown below, (high school math, 7p)
# - consider each 'region' individually
#   - if we put knight 1 in this region, how many ways can we put knight 2?
#
# region breakdown: 1 is corners, 2 is edges, 3 is center
# 1122211
# 1122211
# 2233322
# 2233322
# 2233322
# 1122211
# 1122211
#
# TC: O(n)

small_cases = [-1, 0, 6, 28, 96, 252, 550, 1056, 1848]

def f(k):
    if k <= 8:  # avoid edge cases
        return small_cases[k]

    total = 0
    total += (k - 4)**2 * (k**2 - 9)  # center region (k-4 by k-4)
    total += 4 * ((k**2 - 3) + 2*(k**2 - 4) + (k**2 - 5))  # 4 corners (each 2 by 2)
    total += 4 * ((k - 4) * (k**2 - 5))  # 4 outer edges (each 1 by k-4)
    total += 4 * ((k - 4) * (k**2 - 7))  # 4 inner edges (each 1 by k-4)

    return total // 2  # symmetry


n = int(input())

for k in range(1, n + 1):
    print(f(k))

