// https://cses.fi/problemset/task/3359/
// direct c++ translation
// check Python code for explanation

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    vector<vector<char>> vis(n, vector<char>(n, 0));

    vector<int> q1, q2;
    q1.push_back(0);
    q2.push_back(0);

    string res;
    res.reserve(2 * n);

    for (int le = 1; le < 2 * n; le++) {
        // find minimum character in current layer
        char min_char = 'z';
        for (int i = 0; i < (int)q1.size(); i++) {
            min_char = min(min_char, grid[q1[i]][q2[i]]);
        }
        res.push_back(min_char);

        // keep only positions achieving min_char
        vector<int> nq1, nq2;
        for (int i = 0; i < (int)q1.size(); i++) {
            if (grid[q1[i]][q2[i]] == min_char) {
                nq1.push_back(q1[i]);
                nq2.push_back(q2[i]);
            }
        }
        q1.swap(nq1);
        q2.swap(nq2);

        // expand BFS frontier
        vector<int> nxt1, nxt2;
        for (int i = 0; i < (int)q1.size(); i++) {
            int r = q1[i], c = q2[i];

            if (r + 1 < n && !vis[r + 1][c]) {
                vis[r + 1][c] = 1;
                nxt1.push_back(r + 1);
                nxt2.push_back(c);
            }
            if (c + 1 < n && !vis[r][c + 1]) {
                vis[r][c + 1] = 1;
                nxt1.push_back(r);
                nxt2.push_back(c + 1);
            }
        }

        q1.swap(nxt1);
        q2.swap(nxt2);
    }

    cout << res << '\n';
    return 0;
}
