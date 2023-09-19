class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        dp = [0]*n
        visited1 = [0]*n
        visited1[0] = 1
        
        def dfs(node):
        
            cur_ans = 0
            count = 1
            
            for neigh in graph[node]:
                if not visited1[neigh]:
                    visited1[neigh] = 1
                    a, c = dfs(neigh)
                    count += c
                    cur_ans += a + c
                    
            
            dp[node] = cur_ans, count
            return dp[node]
        
        dfs(0)
        ans = [0]*n
        visited = [0]*n
        visited[0] = 1
        # print(dp)
        
        def dfs2(node, par_ans, par_count):
            
            cur_ans, cur_count = dp[node]
            ans[node] = par_ans + par_count + cur_ans
        
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    neigh_ans, neigh_count = dp[neigh]
                    temp_ans = par_ans + par_count + cur_ans - (neigh_ans + neigh_count)
                    temp_count = cur_count - neigh_count + par_count
                    dfs2(neigh, temp_ans, temp_count)
        
        
        dfs2(0, 0, 0)
        return ans
            
            
            
            
            