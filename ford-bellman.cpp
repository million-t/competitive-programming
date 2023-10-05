#include <iostream>
#include <vector>
#include <climits>

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::vector<std::vector<std::pair<int, int>>> graph(n);

    std::vector<int> dist(n, INT_MAX);
    dist[0] = 0;

    for (int i = 0; i < m; i++) {
        int u, v, w;
        std::cin >> u >> v >> w;
        u--;
        v--;
        graph[u].push_back(std::make_pair(v, w));
    }

    for (int it = 0; it < n - 1; it++) {
        for (int u = 0; u < n; u++) {
            for (auto edge : graph[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }
    }

    for (int ind = 0; ind < n; ind++) {
        if (dist[ind] == INT_MAX) {
            dist[ind] = 30000;
        }
    }

    for (int i = 0; i < n; i++) {
        std::cout << dist[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
