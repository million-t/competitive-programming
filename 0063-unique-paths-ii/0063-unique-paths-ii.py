class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0]*cols for _ in range(rows)]
        
        for row in range(rows):
            val = obstacleGrid[row][0]
            if val:
                break

            else:
                dp[row][0] = 1
        
        for col in range(cols):
            val = obstacleGrid[0][col]
            if val:
                break

            else:
                dp[0][col] = 1
                
        for row in range(1, rows):
            for col in range(1, cols):
                if not obstacleGrid[row][col]:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[-1][-1]
        
        