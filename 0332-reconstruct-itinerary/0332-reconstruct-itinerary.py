class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dest in tickets:
            graph[src].append(dest)
        
        for src in graph:
            graph[src].sort(reverse=True)
        
        
        ans = []
        def dfs(node):
            
            dests = graph[node]
            while dests:
                dfs(dests.pop())
            
            ans.append(node)
        
        dfs('JFK')
        return ans[::-1]
            
            
            