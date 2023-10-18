


n, m = map(int, input().split())


edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
inf = 10**9
dist = [inf]*(n + 1)
path = [None]*(n + 1)


last_modified = None
for _ in range(n):

    last_modified = None
    for node, neigh, weight in edges:
        if dist[node] + weight < dist[neigh]:
            dist[neigh] = dist[node] + weight
            path[neigh] = node
            last_modified = neigh


if last_modified:

    for _ in range(n):
        last_modified = path[last_modified]
    

    visited = set()
    ans = []
    while last_modified not in visited:
        ans.append(last_modified)
        visited.add(last_modified)
        last_modified = path[last_modified]
    
    ans.append(ans[0])
    print('YES')
    print(*ans[::-1])

else:
    print('NO')

