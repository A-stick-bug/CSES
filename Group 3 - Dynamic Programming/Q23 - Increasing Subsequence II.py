# https://cses.fi/problemset/task/1748
# Sequence DP + data structures, 12-15p
#
# dp[idx][last] = number of increasing sequences up to index `idx` and ending with `last`
# We need a range sum query data structure to transition effectively, use Fenwick Tree
#
# TC: O(n*log(n))

class FenwickTree:  # point update, range query, 1-indexed
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            self.bit[i] %= MOD
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total % MOD


MOD = 10 ** 9 + 7
n = int(input())
arr = list(map(int, input().split()))

# coordinate compression
ordered = sorted(set(arr))
compress = {ordered[i]: i + 1 for i in range(len(ordered))}
arr = [compress[val] for val in arr]
m = len(ordered)

dp = FenwickTree(m + 1)
for val in arr:
    dp.update(val, dp.query(val - 1))  # ending with `val`, can extend sequences ending with smaller values
    dp.update(val, 1)  # sequence with only `val`

print(dp.query(m) % MOD)
