# https://cses.fi/problemset/task/1624
# Recursion/backtracking, 7p
#
# Try placing queens at each open location and backtrack if we get contradictions
# Fun alternate solution: hardcode the n-queen solutions and print the ones that don't overlap with *
#
# TC: exponential (hard to analyze exact bound)

n = 8
grid = [list(input()) for _ in range(n)]

rows = [False] * n  # track whether rows/columns/diagonals are occupied
cols = [False] * n
diags = [False] * (2 * n)  # / diagonal
diags2 = [False] * (2 * n)  # \ diagonal

total = 0


def backtrack(idx):
    global total
    if idx == n * n:
        total += sum(rows) == n  # add 1 if we found a valid config
        return

    r, c = divmod(idx, n)
    if grid[r][c] == "*" or rows[r] or cols[c] or diags[r + c] or diags2[r - c]:  # can't place here
        backtrack(idx + 1)
    else:  # try placing here
        rows[r] = cols[c] = diags[r + c] = diags2[r - c] = True
        backtrack(idx + 1)
        rows[r] = cols[c] = diags[r + c] = diags2[r - c] = False

        backtrack(idx + 1)  # also try skipping here


backtrack(0)
print(total)
