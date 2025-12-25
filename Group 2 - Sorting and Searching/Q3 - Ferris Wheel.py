# https://cses.fi/problemset/task/1090
# Greedy + 2 pointers, 7-10p
#
# Key fact: a gondola can only have 2 people max
# - Consider the people from largest weight first, try fitting another person if possible
# - it doesn't matter who we put since everyone after will have a smaller weight and be able to fit them anyway
#
# TC: O(nlogn)

N, X = map(int, input().split())
arr = sorted(map(int, input().split()))

total = N
j = 0
for i in reversed(range(N)):
    if i <= j:
        break
    if arr[i] + arr[j] <= X:
        total -= 1  # fit another person, save a space
        j += 1
print(total)
