class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def inbound(row, col):
            return 0 <= row < len(grid1) and 0 <= col < len(grid1[0])
        
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        

        def dfs(row, col):
            
            if not (inbound(row, col) and grid2[row][col]):
                return True
            
            
            if not grid1[row][col]:
                return False
            
            grid2[row][col] = 0
            value = True
            
            for r_change, c_change in directions:
                if not dfs(row + r_change, col + c_change):
                    value = False
                    
            return value
    
        
        sub_islands = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                
                if grid2[row][col]:
                    sub_islands += dfs(row, col)
        
        return sub_islands
            
            
            
        