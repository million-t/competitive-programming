class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        for node in graph:
            if indegree[node] == 1:
                
                order = []
                queue = deque([node])
                visited = set([node])
                
                while queue:
                    cur = queue.popleft()
                    order.append(cur)
                    
                    for neigh in graph[cur]:
                        if neigh not in visited:
                            queue.append(neigh)
                            visited.add(neigh)

                return order
            
        