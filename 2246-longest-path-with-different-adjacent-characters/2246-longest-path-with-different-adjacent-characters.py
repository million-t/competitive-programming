class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        tree = [[] for _ in range(len(parent))]
        
        for child, par in enumerate(parent):
            if par != -1:
                tree[par].append(child)
        
        longest = 0
        
        def dfs(node):
            nonlocal longest
            
            long_through_cur = 0
            sec_long = 0
            
            for child in tree[node]:
                through_child = dfs(child)
                
                if s[node] != s[child]:
                    sec_long = min(long_through_cur, max(sec_long, through_child))
                    long_through_cur = max(long_through_cur, through_child)
            
            longest = max(longest, long_through_cur + sec_long + 1)
            return long_through_cur + 1
        
        dfs(0)
        
        return longest
        
            