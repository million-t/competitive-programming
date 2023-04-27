class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        visited = set([0])
        def dfs(node): 
            
            time = 0
            
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    time += dfs(child)
                
            if not (time or hasApple[node]):
                return 0
            
            return time + 1
        
        res = dfs(0)
        
        if not res:
            return res
        
        return 2*(res - 1)
            
        