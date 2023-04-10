class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for row in range(len(isConnected)):
            for col in range(row, len(isConnected[0])):
                
                if isConnected[row][col] and row != col:
                    graph[row].append(col)
                    graph[col].append(row)
                
                elif isConnected[row][col]:
                    graph[row].extend([])
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)
        
        
        provinces = 0
        for node in graph:
            
            if node not in visited:
                dfs(node)
                provinces += 1
            
        
        return provinces