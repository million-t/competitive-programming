class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def computeIndex(row, col):
            cols = len(grid[0])
            return row*cols + col
        
        def inbounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        
        def dfs(row, col, visited, target):
            
            if grid[row][col] == 2 and visited == target:
                return 1
            
            elif grid[row][col] == 2:
                return 0
            
            sub_ans = 0
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not inbounds(nr, nc):
                    continue
                
                new_indx = 1 << computeIndex(nr, nc)
                if grid[nr][nc] == -1 or visited & new_indx:
                    continue
                    
                sub_ans += dfs(nr, nc, visited ^ new_indx, target)
                
            return sub_ans
        
        start = (0, 0)
        target = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = (row, col)
                
                if grid[row][col] != -1:
                    target |= 1 << computeIndex(row, col)  
        
        visited = 1 << computeIndex(*start)
        
        return dfs(*start, visited, target)