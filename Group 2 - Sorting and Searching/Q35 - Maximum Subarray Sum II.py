# https://cses.fi/problemset/task/1644
# Data structures + PSA, 10p
#
# First try [G2 Q8 - Maximum Subarray Sum](https://cses.fi/problemset/task/1643)
# Again, think of subarrays as prefix[r] - prefix[l], try all `r` and minimize prefix[l] for each
# Based on the length restriction (a,b) we determine the range of possible previous indices `l`
#
# TC: O(nlogn)
# SC: O(nlogn), ~100mb depending on Python interpreter
# We could get O(n) SC by maintaining a multiset and picking the min, but range query is very clean here
# We could also get O(n) TC using monotonic queues but those are quite unintuitive, and we leave them for later

from itertools import accumulate

log2 = lambda x: x.bit_length() - 1


class SparseTable:  # 0-indexed
    def __init__(self, arr, f=max, default=0):
        N = len(arr)
        self.layers = log2(len(arr)) + 1
        self.table = [[default] * self.layers for _ in range(len(arr))]
        self.f = f
        for i in range(len(arr)):  # base layer
            self.table[i][0] = arr[i]  # column 1: base cases

        for k in range(1, self.layers):  # build the rest of the table
            for i in range(N - (1 << k) + 1):
                self.table[i][k] = f(self.table[i][k - 1], self.table[i + (1 << (k - 1))][k - 1])

    def query(self, l, r):
        k = log2(r - l + 1)
        return self.f(self.table[l][k], self.table[r - (1 << k) + 1][k])


n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

best = -(1 << 60)
psa = [0] + list(accumulate(arr))
st = SparseTable(psa, f=min, default=(1 << 60))
for i in range(a, n + 1):
    l = max(0, i - b)
    r = i - a
    best = max(best, psa[i] - st.query(l, r))
print(best)
