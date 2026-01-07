/*
 https://cses.fi/problemset/task/3314
 Divide and conquer + greedy + data structures, 12-15p
 Similar structure to interval DP, but completely different idea
 Note: This solution uses advanced techniques but is easy to reason about

 Greedy idea: start at a max height
 - Reasoning: if we started somewhere else, we could instead start at a max height and glide there later
   - This applies to subproblems as well
 Divide and conquer idea:
 - At each step, either go left or right to any max height <cur
 - We also restrict the allowed range to ensure we never cross over a taller height
 Use a range max query (RMQ) data structure to determine the max heights

 TC: O(nlogn)
 SC: O(nlogn)
 Possible tradeoff: use segment tree for O(n*log^2(n)) time and O(n) space
 */

#include <bits/stdc++.h>
#define pii pair<int, int>

using namespace std;

const int LOG = 19;
const int MN = 200001;
pii st[LOG][MN];  // (value, -idx), prioritize indices to the left

void build_st(const vector<pii>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++)  // base layer
        st[0][i] = arr[i];
    for (int h = 1; h < LOG; h++)
        for (int i = 0; i < n - (1 << h) + 1; i++)
            st[h][i] = max(st[h - 1][i], st[h - 1][i + (1 << (h - 1))]);
}

pii query(int l, int r){
    int h = __lg(r - l + 1);
    return max(st[h][l], st[h][r - (1 << h) + 1]);
}

int solve(int l, int r) {
    if (l > r) return 0;
    if (l == r) return 1;

    int range_mx = query(l, r).first;
    int idx = l;
    int best = 0;
    while (idx <= r) {  // process all maxima in [l,r]
        auto [mx, nxt] = query(idx, r);
        nxt = -nxt;
        if (mx != range_mx) {  // last one
            best = max(best, 1 + solve(idx, r));
            break;
        } else {
            best = max(best, 1 + solve(idx, nxt - 1));
            idx = nxt + 1;
        }
    }
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<pii> arr(N);  // (value, index)
    for (int i = 0; i < N; i++){
        int x;
        cin >> x;
        arr[i] = {x, -i};
    }

    build_st(arr);
    cout << solve(0, N - 1) << "\n";

    return 0;
}
