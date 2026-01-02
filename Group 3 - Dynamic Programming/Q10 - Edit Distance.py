# https://cses.fi/problemset/task/1639
# Sequence DP, 10-12p
#
# dp[i][j] = minimum moves to turn first `i` in s to first `j` in t
# Insertion is the trickiest, think of it as inserting into a position that matches with `j` in t
# This is equivalent to deleting `j` from t
#
# TC: O(nm)

s = "." + input()  # pad with common prefix
t = "." + input()
n = len(s)
m = len(t)

inf = 1 << 30
dp = [[inf] * (m + 1) for _ in range(n + 1)]  # pad at the end so index -1 gives inf
dp[0][0] = 0

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        else:
            dp[i][j] = min(dp[i][j],
                           dp[i - 1][j - 1] + 1,  # replace
                           dp[i - 1][j] + 1,  # delete
                           dp[i][j - 1] + 1)  # insert to create a match

# for i in dp:
#     print(i)
print(dp[n - 1][m - 1])

# # memory optimized version
# # this one also runs faster
#
# s = "." + input()  # pad with common prefix
# t = "." + input()
# n = len(s)
# m = len(t)
#
# inf = 1 << 30
# dp = list(range(m + 1))
#
# for i in range(1, n):
#     new_dp = [inf] * (m + 1)
#     for j in range(m):
#         if s[i] == t[j]:
#             new_dp[j] = dp[j - 1]
#         else:
#             new_dp[j] = min(dp[j - 1] + 1,  # replace
#                             dp[j] + 1,  # delete
#                             new_dp[j - 1] + 1)  # insert to create a match
#     dp = new_dp
#     # print(dp)
#
# print(dp[m - 1])
