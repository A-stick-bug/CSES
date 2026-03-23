// https://cses.fi/problemset/task/1672
// Template Floyd-Warshall algorithm, 10-12p
//
// TC: O(n^3 + m + q)

#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, Q;
    cin >> N >> M >> Q;

    const ll INF = (1LL << 60);
    vector<vector<ll>> dist(N + 1, vector<ll>(N + 1, INF));

    for (int i = 0; i < M; i++) {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        dist[a][b] = min(dist[a][b], c);
        dist[b][a] = min(dist[b][a], c);
    }
    for (int i = 1; i <= N; i++) {
        dist[i][i] = 0;
    }

    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (dist[i][k] == INF || dist[k][j] == INF)
                    continue;
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    while (Q--) {
        int a, b;
        cin >> a >> b;
        if (dist[a][b] == INF) cout << -1 << '\n';
        else cout << dist[a][b] << '\n';
    }
    return 0;
}
