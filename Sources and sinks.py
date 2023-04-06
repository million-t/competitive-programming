n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


sources = []
sinks = []

for row in range(1, n + 1):
    if not 1 in graph[row - 1]:
        sinks.append(row)

for col in range(1, n + 1):
    
    outdegree = False
    for row in range(1, n + 1):
        
        if graph[row - 1][col - 1]:
            outdegree = True
            break

    if not outdegree:
        sources.append(col)    




sinks.sort()
sources.sort()
print(len(sources), *sources)
print(len(sinks), *sinks)
