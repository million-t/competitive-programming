class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        
        def bfs(node):
            
            queue = deque([node])
            color[node] = 1
            
            while queue:
                
                cur = queue.popleft()
                for neigh in graph[cur]:
                    
                    if color[neigh] != -1:
                        if color[neigh] == color[cur]:
                            return False
                        
                        continue
                    
                    color[neigh] = 1 - color[cur]
                    queue.append(neigh)
            
            return True
        
        
        for node in range(n):
            if color[node] == -1 and not bfs(node):
                return False
        
        return True
        