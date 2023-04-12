class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def distance(x1, y1, x2, y2):
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        graph = defaultdict(list)
        
        for ind, (x1, y1, r1) in enumerate(bombs):
            for jnd, (x2, y2, r2) in enumerate(bombs):
                
                if distance(x1, y1, x2, y2) <= r1:
                    graph[ind].append(jnd)
                
                
        def dfs(node):
            
            visited = set([node])
            stack = [node]
            degree = 1
            
            while stack:
                cur = stack.pop()
                
                for neighbour in graph[cur]:
                    if neighbour not in visited: 
                        degree += 1
                        stack.append(neighbour)
                        visited.add(neighbour)
            
            return degree
        
        max_degree = 0
        for bomb in graph:
            
            max_degree = max(max_degree, dfs(bomb))
            
        return max_degree
        
        
        