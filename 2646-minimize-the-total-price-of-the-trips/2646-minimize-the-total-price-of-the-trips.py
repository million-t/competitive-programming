class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        usage_count = [0]*n
        
        def dfs1(node, target):
            if node == target:
                usage_count[target] += 1
                return True
            
            on_path = False
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    on_path = on_path or dfs1(neigh, target)
            
            usage_count[node] += int(on_path)
            return on_path
        
        for start, end in trips:
            visited = [0]*n
            visited[start] = 1
            dfs1(start, end)
        
        
        visited = [0]*n
        visited[0] = 1
        dp = [0]*n
        temp2 = [0]*n
        
        def dfs2(node):
            
            cost = usage_count[node]*price[node]
            temp = 0

            
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    neigh_cost = dfs2(neigh)
                    dp[node] += max(neigh_cost, dp[neigh])
                    temp += dp[neigh]
            
            return cost + temp
            
            
        
        return sum([ price[i]*usage_count[i] for i in range(n) ]) - (max(dfs2(0), dp[0])//2)
        
                
        