
while True:


    n = int(input())

    if not n:
        break

    graph = [[] for _ in range(n)]

    l = int(input())
    for _ in range(l):
        a, b = map(int, input().split())

        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)


    bICOLOURABLE = True

    color = [-1]*n
    color[0] = 1

    stack = [(0, 1)]

    while stack:
        node, cur_color = stack.pop()

        nei_color = 1 - cur_color
        for neighbor in graph[node]:

            if color[neighbor] != -1:
                if color[neighbor] != nei_color:
                    bICOLOURABLE = False
                    break

            else:
                stack.append((neighbor, nei_color))
                color[neighbor] = nei_color

    if bICOLOURABLE:
        print('BICOLOURABLE.')

    else:
        print('NOT BICOLOURABLE.')
