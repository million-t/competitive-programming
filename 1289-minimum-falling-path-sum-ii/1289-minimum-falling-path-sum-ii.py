class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        
        
        for row in range(1, rows):
            
            preffix = [float('inf')]
            sufix = [float('inf')]*(columns + 1)
            for col in range(columns):
                preffix.append(min(preffix[-1], grid[row - 1][col]))
            
            for col in range(columns - 1, -1, -1):
                sufix[col] = min(sufix[col + 1], grid[row - 1][col])
            
            for col in range(columns):
                grid[row][col] += min(preffix[col], sufix[col + 1])
                
        
        
        return min(grid[-1])
        