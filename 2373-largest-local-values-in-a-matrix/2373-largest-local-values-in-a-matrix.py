class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def helper(r, c):
            maxx = 0
            for row in [-1, 0, 1]:
                for col in [-1, 0, 1]:
                    maxx = max(maxx, grid[r + row][c + col])
                    
            return maxx
        
        n = len(grid)
        
        maxLocal = [ [0]*(n-2) for _ in range(n - 2)]
        
        for row in range(n-2):
            for col in range(n-2):
                maxLocal[row][col] = helper(row + 1, col + 1)
        return maxLocal
        
        