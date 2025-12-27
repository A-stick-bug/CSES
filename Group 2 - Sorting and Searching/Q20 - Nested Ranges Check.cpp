// https://cses.fi/problemset/task/2168
// Intervals, 10p
//
// The trick is sorting the intervals in a specific order
// TC: O(nlogn)

#include <bits/stdc++.h>

using namespace std;

int n;
vector<array<int, 3>> arr;

void solve_contains() {
    sort(arr.begin(), arr.end(), [&](auto a, auto b) {  // sort by (r ascending, l descending)
        return pair{a[1], -a[0]} < pair{b[1], -b[0]};
    });

    vector<int> ans(n, 0);
    int max_left = -1;
    for (auto [l, r, i]: arr) {
        if (l <= max_left)  // covers previous, since prev_r <= r by sorting
            ans[i] = 1;
        max_left = max(max_left, l);
    }
    for (int i = 0; i < n; i++)
        cout << ans[i] << " \n"[i == n - 1];
}

void solve_contained() {
    sort(arr.begin(), arr.end(), [&](auto a, auto b) {  // sort by (l ascending, r descending)
        return pair{a[0], -a[1]} < pair{b[0], -b[1]};
    });

    vector<int> ans(n, 0);
    int max_right = -1;
    for (auto [l, r, i]: arr) {
        if (r <= max_right)  // covered by previous, since prev_l <= l by sorting
            ans[i] = 1;
        max_right = max(max_right, r);
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
