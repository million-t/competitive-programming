class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        
        target = 1
        for pos in range(len(graph) - 1):
            target <<= 1
            target ^= 1
        
        ans = float("inf")
        for start in range(len(graph)):
            
            visited = set([(start, 1<<start)])
            queue = deque( [(start, 1<<start)] )
            moves = 0
            found = False
            
            while queue and (not found) and moves < ans:
                for _ in range(len(queue)):
                    node, path = queue.popleft()

                    if path == target:
                        found = True
                        ans = min(ans, moves)
                        break

                    for neigh in graph[node]:
                        path_copy = path
                        temp = 1 << neigh
                        path_copy |= temp
                        if (neigh, path_copy) not in visited:
                            queue.append((neigh, path_copy))
                            visited.add((neigh, path_copy))
                moves += 1     

        
        return ans
        