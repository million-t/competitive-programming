class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for num1, num2 in dislikes:
            graph[num1].append(num2)
            graph[num2].append(num1)
        
        
        
        group = [-1]*n
        visited = set()
        
        def dfs(node, cur_group):
            
            if node in visited:
                return True
            
            visited.add(node)
                
            
            for neighbour in graph[node]:
                
                if group[neighbour - 1] == -1:
                    group[neighbour - 1] = 1 - cur_group
                    
                    if not dfs(neighbour, group[neighbour - 1]):
                        return False
                
                elif group[neighbour - 1] == group[node - 1]:
                    return False 
                
            
            return True
        
        
        
        for node in graph:
            if node not in visited:
                
                if not dfs(node, 1):
                    return False
        
        return True