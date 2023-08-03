class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        rows, cols = len(grid), len(grid[0])
        dp = [defaultdict(set) for _ in range(rows + 1)]
        
        for ind in range(cols):
            dp[0][ind].add(ind)
            
        for row in range(rows):
            for col in range(cols):
                diag = grid[row][col]
                
                if diag == 1 and col < cols - 1 and grid[row][col + 1] != -1:
                    dp[row + 1][col + 1].update(dp[row][col])
                
                elif diag == -1 and col > 0 and grid[row][col - 1] != 1:
                    dp[row + 1][col - 1].update(dp[row][col])
        
        
        
        
        ans = [-1]*cols
        
        for ind, _set in dp[-1].items():
            for item in _set:
                ans[item] = ind
                    
        return ans
                    
                    
                
        