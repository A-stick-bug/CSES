# https://cses.fi/problemset/task/2413
# Sequence DP, 12p
#
# Note that there are `t` cases, so we try to compute once and use the same dp table for each case
# dp[split?][x] = number of ways to make a tower of height x
# - if split, the top layer has 2 independent (1x1) blocks, if not, it is 1 joined (1x2) block
# - putting the smaller dimension outside is more efficient
#
# TC: O(n + t)
# Note: a O(t * log(n)) solution is presented below

n = 10 ** 6 + 1
MOD = 10 ** 9 + 7

dp = [[0] * (n + 1) for _ in range(2)]
dp[0][1] = dp[1][1] = 1  # base cases: 1 joined (1x2) block, or 2 independent (1x1) blocks
for x in range(2, n + 1):
    dp[0][x] += 2 * dp[0][x - 1] + dp[1][x - 1]
    dp[1][x] += 4 * dp[1][x - 1] + dp[0][x - 1]

    dp[0][x] %= MOD
    dp[1][x] %= MOD

# for i in dp:
#     print(i)

t = int(input())
for _ in range(t):
    n = int(input())
    print((dp[0][n] + dp[1][n]) % MOD)

# # Solution 2
# # Matrix exponentiation, 15p
# # Note that the recurrence is linear and has very few terms
# # we can efficiently use matrices to get O(log(n)) per test case
# # TC: O(t * log(n))
# MOD = 10 ** 9 + 7
#
#
# def multiply(m2, m1):
#     n = len(m1)
#     m3 = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):  # j -> idx -> i
#             m3[i][j] = sum(m1[idx][j] * m2[i][idx] for idx in range(n)) % MOD
#     return m3
#
#
# def matrix_exp(original_mat, p):
#     n = len(original_mat)
#     base = [row.copy() for row in original_mat]
#     res = [[0] * n for _ in range(n)]  # identity matrix
#     for i in range(n):
#         res[i][i] = 1
#     while p > 0:
#         if p % 2 == 1:
#             res = multiply(base, res)
#         base = multiply(base, base)
#         p //= 2
#
#     return res
#
#
# mat = [[4, 1], [1, 2]]
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#
#     res = matrix_exp(mat, n - 1)
#     print(sum(sum(row) for row in res) % MOD)
