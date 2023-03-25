class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for vertex1, vertex2 in edges:
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)
        
        
        visited = set()
        
        queue = deque([source])
        
        while queue:
            
            cur_node = queue.popleft()
            
            if cur_node == destination:
                return True
            
            if cur_node not in visited:
                visited.add(cur_node)
                
                for neighbour in graph[cur_node]:
                    queue.append(neighbour)
        
        return False