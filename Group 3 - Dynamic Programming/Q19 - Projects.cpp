// https://cses.fi/problemset/task/1140
// Sequence DP (task scheduling) + data structures, 12p
//
// DP method: sort by start and let dp[i] = max money at i
// This guarantees we processed every possible previous state
// We use a Fenwick tree to query the intervals ending at less than start
// Note: could also maintain a heap that store ends and pop at each start
//
// Note: I just realized you can simply use line sweep here and avoid all data structures
// - at start events, set dp[idx] = current max + money
// - at end events, update the current max with dp[idx]
//
// TC: O(nlogn)

#include <bits/stdc++.h>
#define int long long

using namespace std;

class FenwickTree {  // prefix max queries only
public:
    vector<int> bit;
    int N;

    FenwickTree(int n) {
        N = n;
        bit = vector<int>(N + 1, 0);
    }

    void update(int i, int val) {
        for (; i < bit.size(); i += i & -i) {
            bit[i] = max(bit[i], val);
        }
    }

    int query(int i) {
        int total = 0;
        for (; i > 0; i -= i & -i) {
            total = max(total, bit[i]);
        }
        return total;
    }
};


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<array<int, 3>> arr(n);
    vector<int> coords;
    for (int i = 0; i < n; i++) {
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
        coords.push_back(arr[i][0]);
        coords.push_back(arr[i][1]);
    }

    sort(arr.begin(), arr.end(), [&](auto a, auto b) {
        return a[0] < b[0];  // by start
    });

    // coordinate compression
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    int m = coords.size();
    for (auto &x: arr) {
        x[0] = 1 + lower_bound(coords.begin(), coords.end(), x[0]) - coords.begin();
        x[1] = 1 + lower_bound(coords.begin(), coords.end(), x[1]) - coords.begin();
    }

    FenwickTree bit(m + 1);
    for (auto [l, r, val]: arr) {
        int cur = bit.query(l - 1) + val;  // previous max
        bit.update(r, cur);  // update by endpoint
    }

    cout << bit.query(m) << "\n";
    return 0;
}
