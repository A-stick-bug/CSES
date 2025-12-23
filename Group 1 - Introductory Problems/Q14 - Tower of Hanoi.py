# https://cses.fi/problemset/task/2165
# Recursion, 7p
#
# We don't formally prove, but it is easy to see why 2^n-1 moves looks optimal
# Look at this animation to find a pattern https://www.mathsisfun.com/games/towerofhanoi.html
#
# TC: O(2^n)

def gen_moves(n, start, finish, other):
    # generates moves to move a pile [n,n-1,...,1] from start to finish using the other pile
    if n == 1:
        return [[start, finish]]
    moves = gen_moves(n - 1, start, other, finish)  # clear out everything on top of n
    moves.append([start, finish])  # move number n
    moves.extend(gen_moves(n - 1, other, finish, start))  # move everything back on top of n
    return moves


n = int(input())

print(2 ** n - 1)
for move in gen_moves(n, 1, 3, 2):
    print(*move)
