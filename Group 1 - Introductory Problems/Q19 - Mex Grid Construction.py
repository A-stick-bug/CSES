# https://cses.fi/problemset/task/3419
# Solution 1 (shown below): Implementation, 5p, TC: O(n^3)
# - Literally do as the question says, use set to speed up MEX calculation
#
# Solution 2: Observe the pattern or use OEIS: https://oeis.org/A003987
# - Around 7p, actually understanding the math behind it is way harder

# Solution 1

def mex(arr):
    unique = set(arr)
    for i in range(len(unique) + 1):
        if i not in unique:
            return i
    return None


n = int(input())
grid = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        left = grid[i][:j]
        above = [grid[k][j] for k in range(i)]
        grid[i][j] = mex(left + above)

for row in grid:
    print(*row)

# # Solution 2
#
# n = int(input())
# grid = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         grid[i][j] = i ^ j
# for row in grid:
#     print(*row)
