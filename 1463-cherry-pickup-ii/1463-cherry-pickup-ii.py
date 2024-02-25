class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def inbounds(pt1):
            return 0 <= pt1 < m 
        
        @cache
        def dp(left, right, level):
            if level == n - 1:
                if left == right:
                    return grid[level][left]
                
                return grid[level][left] + grid[level][right]
            
            
            val = grid[level][left] + grid[level][right]
            if left == right:
                val -= grid[level][right]
                
            ans = dp(left, right, level + 1)
            if inbounds(left - 1):
                ans = max(ans, dp(left - 1, right, level + 1))
                ans = max(ans, dp(left - 1, right - 1, level + 1))
            
            if left <= right - 1:
                ans = max(ans, dp(left, right - 1, level + 1))
                
            if inbounds(right + 1):
                ans = max(ans, dp(left, right + 1, level + 1))
                ans = max(ans, dp(left + 1, right + 1, level + 1))
            
            if left + 1 <= right:
                ans = max(ans, dp(left + 1, right, level + 1))
            
            if left + 1 <= right - 1:
                ans = max(ans, dp(left + 1, right - 1, level + 1))
            
            if inbounds(left - 1) and inbounds(right + 1):
                ans = max(ans, dp(left - 1, right + 1, level + 1))
            
            return ans + val
        
        return dp(0, m - 1, 0)
                
                          
        
        
        