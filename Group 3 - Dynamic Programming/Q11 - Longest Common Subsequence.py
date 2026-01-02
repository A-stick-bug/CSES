# https://cses.fi/problemset/task/3403
# 2D Sequence DP + reconstruction, 10p
#
# dp[i][j] = LCS of first `i` of a1 and first `j` of a2
# TC: O(nm)

n, m = map(int, input().split())
a1 = [-1] + list(map(int, input().split())) + [-2]  # pad with common elements for easy reconstruction
a2 = [-1] + list(map(int, input().split())) + [-2]

dp = [[0] * (m + 2) for _ in range(n + 2)]
dp[0][0] = 1
prev = [[-1] * (m + 2) for _ in range(n + 2)]  # track the transitions

for i in range(1, n + 2):
    for j in range(1, m + 2):
        if a1[i] == a2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            prev[i][j] = 0
        if dp[i - 1][j] > dp[i][j]:
            dp[i][j] = dp[i - 1][j]
            prev[i][j] = 1
        if dp[i][j - 1] > dp[i][j]:
            dp[i][j] = dp[i][j - 1]
            prev[i][j] = 2

seq = []  # reconstruct
i = n + 1
j = m + 1
while i != 0 and j != 0:
    if prev[i][j] == 0:
        seq.append(a1[i])
        i -= 1
        j -= 1
    elif prev[i][j] == 1:
        i -= 1
    else:
        j -= 1

print(len(seq) - 1)  # last element is padding
print(*seq[::-1][:-1])
