class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        people = len(quiet)
        graph = [[] for _ in range(people)]
        
        for a, b in richer:
            graph[b].append(a)
        
        ans = list(range(people))
        color = [0]*people
        
        def topoSort(cur):
            
            if color[cur]:
                return
            
            color[cur] = 1
            for neigh in graph[cur]:
                
                topoSort(neigh)
                if quiet[ans[neigh]] < quiet[ans[cur]]:
                    ans[cur] = ans[neigh]
        
        for node in range(people):
            topoSort(node)
        
        return ans
                
                