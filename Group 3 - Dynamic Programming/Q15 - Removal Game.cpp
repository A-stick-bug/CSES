// https://cses.fi/problemset/task/1097
// Game theory + interval DP, 10-12p
//
// Assuming they play until all numbers are removed
// One player's score determines the other's since sum is fixed
// - Track only player 1's score: P1 tries to maximize, P2 tries to minimize
//
// dp[l][r] = result of subgame on arr[l] to arr[r]
//
// TC: O(n^2)

#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<vector<ll>> dp(n, vector<ll>(n));
    for (int i = 0; i < n; i++)
        dp[i][i] = (n % 2 == 0) ? 0 : arr[i];  // base cases

    for (int le = 2; le <= n; le++) {
        for (int l = 0; l + le - 1 < n; l++) {
            int r = l + le - 1;
            if ((n - le) % 2 == 0) {
                dp[l][r] = max(arr[l] + dp[l + 1][r],  // player 1's turn
                               arr[r] + dp[l][r - 1]);
            } else {
                dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]);  // player 2's turn
            }

        }
    }
    cout << dp[0][n - 1] << "\n";

    return 0;
}
