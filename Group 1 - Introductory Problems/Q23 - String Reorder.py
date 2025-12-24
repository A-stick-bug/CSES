# https://cses.fi/problemset/task/1743
# Greedy algorithms, 10p
#
# Want lex min -> greedily build string from left to right
# - We try placing the min character at each index, as long as we can still make the rest of the string
# - Thus, we need a fast way to check if we can build a string with no 2 equal adjacent characters
#   - Check if max(freq) - 1 <= sum(freq, excluding the max)
#   - Edge case: if the max character is equal to the previous one, we need 1 more
#     - apparently this case is never reached since building the string would already be impossible
# - Implementing this directly results in a constant factor of 26^2, somehow passes in Python
#
# TC: O(26^2 * n)

import sys


def is_possible(prev, freq):  # check if we can make a valid suffix with freq
    mx = max(freq)
    m_char = freq.index(mx)
    total = sum(freq)
    if m_char == prev:
        return mx <= total - mx
    else:
        return mx - 1 <= total - mx


s = input()
n = len(s)

freq = [0] * 26
for char in s:
    freq[ord(char) - ord('A')] += 1

if not is_possible(-1, freq):
    print(-1)
    sys.exit()

res = [-1] * n
for i in range(n):
    for c in range(26):
        if i != 0 and c == res[i - 1]:
            continue
        if freq[c] == 0:
            continue
        new_freq = freq.copy()
        new_freq[c] -= 1
        if is_possible(c, new_freq):
            res[i] = c
            freq[c] -= 1
            break

res = list(map(lambda x: chr(x + ord('A')), res))
print(''.join(res))
