# https://cses.fi/problemset/task/2205
# Constructive, 10p
#
# We make heavy use of visualizations:
# - Treat the strings as numbers (in binary) for easier interpretation
# - Consider a graph with edges between all numbers with hamming distance 1
# - Notice that it is a hypercube graph, and we need a Hamiltonian path
# - Draw out a hypercube and find the pattern
#
# TC: O(n * 2^n)

n = int(input())

res = [0]
for p2 in range(n):  # this is the pattern I found based off a 4D cube, other constructions likely exist
    res += [i + len(res) for i in res][::-1]

for i in res:
    print(bin(i)[2:].zfill(n))
