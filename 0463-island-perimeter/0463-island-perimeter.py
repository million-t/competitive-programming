class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        def dfs(row, col):
            if (row, col) in visited:
                return 0
            
            if not (inbound(row, col) and grid[row][col]):
                return 1
            
            visited.add((row, col))
            cur_per = 0
            for row_change, col_change in directions:
                
                new_row = row + row_change
                new_col = col + col_change
                cur_per += dfs(new_row, new_col)
            
            return cur_per
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col]:
                    return dfs(row, col)
            
        