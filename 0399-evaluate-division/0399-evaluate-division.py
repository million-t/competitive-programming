class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        def bfs(a, b):
            
            if a not in graph or b not in graph:
                return float(-1)
            
            visited = set([a])
            queue = deque([(a, 1)])
            
            
            while queue:
                size = len(queue)
                for _ in range(size):
                    
                    cur, val = queue.popleft()
                    if cur == b:
                        return val
                    
                    for neigh, quot in graph[cur]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append((neigh, val*quot))
            
            return float(-1)
        
        
        ans = []
        for a, b in queries:
            ans.append(bfs(a, b))
        
        return ans