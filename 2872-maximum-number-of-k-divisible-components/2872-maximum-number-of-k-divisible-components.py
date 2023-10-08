class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        
        
        
        dp = [0]*n
        tree = [[] for _ in range(n)]
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def dfs(node):
            
            temp = values[node]
            for neigh in tree[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    temp += dfs(neigh)
            
            dp[node] = temp
            return temp
        
        
        visited = set([0])
        dfs(0)
        visited = set([0])
        
        def dfs2(node, par_val):
            ans = int(not dp[node]%k and not par_val%k)
            
            for neigh in tree[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    ans += dfs2(neigh, par_val + dp[node] - dp[neigh])
            
            return ans
        
        return dfs2(0, 0)
            
        
        
        
        
        