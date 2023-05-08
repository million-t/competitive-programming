class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        color = [0]*len(graph)
        
        
        def topoSort(graph, cur, color):
            
            if color[cur] == 1:
                return False
            
            if color[cur] == 2:
                return True
            
            color[cur] = 1
            for neigh in graph[cur]:
                
                if not topoSort(graph, neigh, color):
                    return False
            
            color[cur] = 2
            return True
            
            
        
        
        safe_nodes = []
        for node in range(len(graph)):
            if topoSort(graph, node, color):
                safe_nodes.append(node)
            
        
        return safe_nodes