// https://cses.fi/problemset/task/1635
// Knapsack DP (counting ver.), 7p
//
// This is basically [G3 Q1 - Dice Combinations](https://cses.fi/problemset/task/1633) with more dice faces
// dp[x] = number of ways to make a sum of x
// TC: O(n * X)

#include <bits/stdc++.h>
#define ll long long

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

    vector<ll> dp(X + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= X; i++) {
        for (int coin: arr){
            if (i >= coin)
                dp[i] += dp[i - coin];
        }
        dp[i] %= MOD;
    }
    cout << dp[X] << "\n";
    return 0;
}
