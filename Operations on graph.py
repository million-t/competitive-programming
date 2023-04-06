from collections import defaultdict

graph = defaultdict(list)


def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)


def vertex(u):
    print(*graph[u])



n = int(input())
k = int(input())

for _ in range(k):
    operation = list(map(int, input().split()))

    if len(operation) == 3:
        add_edge(operation[1], operation[2])

    else:
        vertex(operation[-1])
