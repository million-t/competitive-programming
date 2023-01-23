class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                p = (i*n + j + k)%(m*n)
                ans[p//n][p%n] = grid[i][j]
            
        return ans
        
        