# https://cses.fi/problemset/task/3311
# Constructive, 5p
#
# Consider filling row by row, left to right
# - At any cell, the character must be different from the one to the left, above, and in the input
# - We ignore the adjacency below and to the right, as we will deal with those once we get there
# - 3 restrictions, 4 choices -> we always have a possible character
#
# TC: O(RC)

R, C = map(int, input().split())
grid = [input() for _ in range(R)]

res = [[""] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        restrict = [grid[i][j]]
        if i != 0:
            restrict.append(res[i - 1][j])
        if j != 0:
            restrict.append(res[i][j - 1])

        for char in "ABCD":
            if char not in restrict:
                res[i][j] = char
                break

for row in res:
    print("".join(row))
