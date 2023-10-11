from collections import defaultdict
from heapq import heappop, heappush


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    x = list(map(int, input().split()))

    temp = defaultdict(list)
    graph = defaultdict(set)
    # ladders = set
    
    for line in range(k):
        a, b, c, d, h = map(int, input().split())
        temp[(a, b)].append((c, d, h))
        graph[a].add(b)
        graph[c].add(d)
        
    graph[n].add(m)
    graph[1].add(1)
    dp = defaultdict(lambda:float('-inf'))
    dp[(1, 1)] = 0
    
    for floor in graph:
        graph[floor] = sorted(graph[floor])

    
    for floor in range(1, n + 1):
        for ind in range(1, len(graph[floor])):
            prev_room = graph[floor][ind - 1]
            room = graph[floor][ind]
            dp[(floor, room)] = max(dp[(floor, room)], dp[(floor, prev_room)] - x[floor - 1]*(room - prev_room))
    
        for ind in range(len(graph[floor]) - 2, -1, -1):
            prev_room = graph[floor][ind + 1]
            room = graph[floor][ind]
            dp[(floor, room)] = max(dp[(floor, room)], dp[(floor, prev_room)] - x[floor - 1]*(prev_room - room))
            

        for ind in range(len(graph[floor])):
            room = graph[floor][ind]
            if (floor, room) in temp:
                for c, d, h in temp[(floor, room)]:
                    dp[(c, d)] = max(dp[(c, d)], dp[(floor, room)] + h)


    ans = -dp[(n, m)]
    
    print( ans if ans != float('inf') else 'NO ESCAPE')


