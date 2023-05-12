class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        graph = [[] for _ in range(len(edges))]
        color = [0]*len(edges)
        
        for ind, node in enumerate(edges):
            if node != -1:
                graph[ind].append(node)
            
        
        index = [0]*len(edges)
        def topoSort(cur, cur_ind):
            
            if color[cur] == 1:
                if index[cur]:
                    return cur_ind - index[cur]
                
                return -1
            
            if color[cur] == 2:
                return -1
            
            color[cur] = 1
            index[cur] = cur_ind
            
            max_nodes = -1
            for neigh in graph[cur]:
                max_nodes = max(topoSort(neigh, cur_ind + 1), max_nodes)
            
            index[cur] = 0
            color[cur] == 2
            return max_nodes
        
        max_cycle = -1
        for node in range(len(edges)):
            if not color[node]:
                max_cycle = max(max_cycle, topoSort(node, 1))
        
            
        return max_cycle
        