# https://cses.fi/problemset/task/1163
# Data structures, 10p
#
# Process in reverse (start with all lights and remove one by one, combine intervals after removing)
# Option 1 (TLE in Python): Keep track of intervals in a SortedList and maintain max length after each combine
# Option 2 (shown below): use a regular list that is sorted + disjoint set to combine intervals
#
# TC: O(nlogn)
# Note that the constant factor is extremely low, as the log is from sorting/binary search
# rather than maintaining a data structure

from bisect import bisect_left


class DisjointSet:
    def __init__(self, N, lengths):  # augmented to also store length of segment
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        self.length = lengths

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.length[root_a] += self.length[root_b]


def solve():
    X, N = map(int, input().split())
    arr = list(map(int, input().split()))

    intervals = []  # ranges [l,r)
    ordered = [0] + sorted(arr) + [X]
    for i in range(N + 1):
        intervals.append([ordered[i], ordered[i + 1]])
    longest = max(r - l for l, r in intervals)

    ds = DisjointSet(len(intervals), [r - l for l, r in intervals])

    intervals = [l for l, r in intervals]  # no longer need right side, only keep left to speed up bisect_left

    ans = [0] * N
    ans[-1] = longest

    for i in reversed(range(1, N)):  # remove 1 at a time
        pos = arr[i]
        idx = bisect_left(intervals, pos)
        ds.union(idx - 1, idx)

        longest = max(longest, ds.length[ds.find(idx)])
        ans[i - 1] = longest

    print(" ".join(map(str, ans)))


solve()
