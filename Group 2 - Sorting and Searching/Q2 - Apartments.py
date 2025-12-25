# https://cses.fi/problemset/task/1084
# Greedy, 7p
#
# Loop people in increasing order of preference
# Each person should take the smallest acceptable one to save the bigger ones for the rest
#
# TC: O(nlogn + mlogm)

n, m, k = map(int, input().split())
arr = sorted(map(int, input().split()))
sizes = sorted(map(int, input().split()))

matches = 0
j = 0
for i in range(n):
    while j < m and sizes[j] < arr[i] - k:
        j += 1
    if j >= m:
        break

    if sizes[j] <= arr[i] + k:
        matches += 1
        j += 1

print(matches)
