from collections import defaultdict

n = int(input())


graph = defaultdict(list)

for _ in range(1, n + 1):
    row = list(map(int, input().split()))

    for ind, con in enumerate(row):
        if con:
            graph[_].append(ind + 1)


for neighbours in graph.values():
    print(len(neighbours), *neighbours)
