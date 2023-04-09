n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


roads = 0
for row in range(n - 1):
    for col in range(row + 1, n):
        roads += graph[row][col]

print(roads)
