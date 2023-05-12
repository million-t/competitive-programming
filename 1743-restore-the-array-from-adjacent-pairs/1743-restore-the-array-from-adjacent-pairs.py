class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        size = len(adjacentPairs) + 1
        graph = defaultdict(list)
        
        
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        
        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        
        arr = []
        color = set()
        
        def topoSort(cur):
            
            if cur in color:
                return
            
            arr.append(cur)   
            color.add(cur)
            
            for neigh in graph[cur]:
                topoSort(neigh)
        
        topoSort(start)
        
        return arr