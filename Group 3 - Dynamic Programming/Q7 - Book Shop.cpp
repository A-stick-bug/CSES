// https://cses.fi/problemset/task/1158
// 0/1 Knapsack DP, 7p
// This is the classic knapsack problem
//
// dp[x] = maximum pages obtainable with cost x
// TC: O(n * X)

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, X;
    cin >> n >> X;
    vector<int> cost(n), value(n);
    for (int i = 0; i < n; i++) cin >> cost[i];
    for (int i = 0; i < n; i++) cin >> value[i];

    vector<int> dp(X + 1, 0);
    for (int i = 0; i < n; i++) {
        int c = cost[i], v = value[i];
        for (int x = X; x >= c; x--) {
            dp[x] = max(dp[x], dp[x - c] + v);
        }
    }
    cout << dp[X] << "\n";
    return 0;
}
