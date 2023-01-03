class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = {}
        for row in grid:
            row = tuple(row)
            count[row] = count.get(row, 0) + 1
        
        ans = 0
        for col in range(n):
            colVal = []
            for row in range(n):
                colVal.append(grid[row][col])
            ans += count.get(tuple(colVal), 0)
        return ans
                
        
            
        