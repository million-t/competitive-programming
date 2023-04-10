class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        visited = set()
        max_area = 0
        
        def dfs(row, col):
            
            if (row, col) in visited or (not inbound(row, col)) or not grid[row][col]:
                return 0
            
            visited.add((row, col))
            area = 1
            for r_change, c_change in directions:
                area += dfs(row + r_change, col + c_change)
                
            return area
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if (row, col) not in visited and grid[row][col]:
                    max_area = max(max_area, dfs(row, col))
                    
        
        return max_area