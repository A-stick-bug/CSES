# https://cses.fi/problemset/task/1653
# Bitmask DP, 15p
#
# dp[mask] = (minimum elevator rides used, minimum weight in current elevator)
# Transition by adding 1 individual person at a time (instead of entire group)
#
# Since using tuple/list of 2 ints is slow, we pack them into 1
# - Notice that when we take min, we still prioritize `# of rides`
#
# TC: O(n * 2^n)

# packing 32-bit integers
def pack(first, second):
    return (first << 32) | second


def unpack(pair):
    return pair >> 32, pair & ((1 << 32) - 1)


def solve():
    inf = 1 << 30
    n, X = map(int, input().split())
    weight = list(map(int, input().split()))

    dp = [pack(inf, inf) for _ in range(1 << n)]
    dp[0] = pack(0, X)  # base case

    for mask in range(1 << n):
        cur = mask
        while cur:  # loop set bits of mask, consider adding i-th person
            i = (cur & (-cur)).bit_length() - 1

            prev_amt, prev_w = unpack(dp[mask - (1 << i)])
            if prev_w + weight[i] > X:
                dp[mask] = min(dp[mask], pack(prev_amt + 1, weight[i]))  # new ride
            else:  # add to old
                dp[mask] = min(dp[mask], pack(prev_amt, prev_w + weight[i]))

            cur -= 1 << i

    print(unpack(dp[(1 << n) - 1])[0])


solve()
