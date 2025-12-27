// https://cses.fi/problemset/task/2169
// Data structures + intervals (1D line sweep), 12p
//
// First see [G2 Q20 - Nested Ranges Check](https://cses.fi/problemset/task/2168)
// Instead of only tracking the max left/right, track all of them in a data structure
// Note that the indexed_set removes duplicates so we must insert both the position and unique id
//
// TC: O(nlogn)

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

template <typename T>
using indexed_set =
    tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

int n;
vector<array<int, 3>> arr;

void solve_contains() {
    sort(arr.begin(), arr.end(), [&](auto a, auto b) {  // sort by (r ascending, l descending)
        return pair{a[1], -a[0]} < pair{b[1], -b[0]};
    });

    vector<int> ans(n, 0);
    indexed_set<pair<int, int>> prev_l;
    for (auto [l, r, i]: arr) {
        // count how many have l <= prev_l (note that prev_r <= r is guaranteed by sorting)
        int idx = prev_l.order_of_key({l, -1});
        ans[i] = prev_l.size() - idx;
        prev_l.insert({l, i});
    }
    for (int i = 0; i < n; i++)
        cout << ans[i] << " \n"[i == n - 1];
}

void solve_contained() {
    sort(arr.begin(), arr.end(), [&](auto a, auto b) {  // sort by (l ascending, r descending)
        return pair{a[0], -a[1]} < pair{b[0], -b[1]};
    });

    vector<int> ans(n, 0);
    indexed_set<pair<int, int>> prev_r;
    for (auto [l, r, i]: arr) {
        // count how many have r <= prev_r (note that prev_l <= l is guaranteed by sorting)
        int idx = prev_r.order_of_key({r, -1});
        ans[i] = prev_r.size() - idx;
        prev_r.insert({r, i});
    }
    for (int i = 0; i < n; i++)
        cout << ans[i] << " \n"[i == n - 1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++) {
        int l, r;
        cin >> l >> r;
        arr[i] = {l, r, i};
    }

    solve_contains();
    solve_contained();

    return 0;
}
