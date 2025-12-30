// https://cses.fi/problemset/task/1636
// Unbounded knapsack DP (counting ver.), 10p
//
// Looks similar to [G3 Q3 - Coin Combinations I](https://cses.fi/problemset/task/1635) but different logic
// dp[x] = number of ways to make a sum of x
// note that we flip the order of the for loop to consider each coin as unbounded knapsack individually
//
// TC: O(n * X)

#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, X;
    cin >> n >> X;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    vector<int> dp(X + 1, 0);
    dp[0] = 1;

    for (int coin: arr) {
        for (int i = coin; i <= X; i++) {
            dp[i] += dp[i - coin];
            dp[i] %= MOD;
        }
    }
    cout << dp[X] << "\n";
    return 0;
}
