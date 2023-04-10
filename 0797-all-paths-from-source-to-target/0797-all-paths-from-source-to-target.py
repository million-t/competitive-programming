class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        destination = len(graph) - 1
        paths = []
        path = [0]
        
        def dfs(node, destination):
            
            if node == destination:
                paths.append(path[:])
                return
            
            
            for neighbour in graph[node]:
                path.append(neighbour)
                dfs(neighbour, destination)
                path.pop()
        
        dfs(0, destination)
        
        return paths