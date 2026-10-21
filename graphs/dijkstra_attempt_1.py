
G = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0 -> 1, 
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # 1 -> 2, 1 -> 3
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], # 2 -> 4, 2 -> 5
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], # 3 -> 6, 3 -> 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4  
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # 6 -> 7
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # 8 -> 9, 8 -> 10
    [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0], # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10
]

# Dijkstra
def dijkstra(G, s, t):
    n = len(G)
    dist = [float('inf')] * n
    dist[s] = 0
    prev = [None] * n
    visited = [False] * n

    for _ in range(n):
        u = min((d, idx) for idx, d in enumerate(dist) if not visited[idx])[1]
        visited[u] = True

        for v, weight in enumerate(G[u]):
            if weight > 0 and not visited[v]:
                alt = dist[u] + weight
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    path = []
    u = t
    while u is not None:
        path.insert(0, u)
        u = prev[u]

    return path if path[0] == s else []

path = dijkstra(G, 0, 10)
print(path)