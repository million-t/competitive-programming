class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        row_max = defaultdict(int)        
        col_max = defaultdict(int)

        
        for row in range(rows):
            for col in range(cols):
                
                cur = grid[row][col]
                row_max[row] = max(row_max[row], cur)
                col_max[col] = max(col_max[col], cur)
        
        ans = 0
        for row in range(rows):
            for col in range(cols):
                cur = grid[row][col]
                ans += max(0, min(row_max[row], col_max[col]) - cur)
        
        return ans
                