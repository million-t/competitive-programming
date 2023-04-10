class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def is_inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        visited = set()
        def dfs(row, col, source_color, change):
            
            if (row, col) in visited or not (is_inbound(row, col) and source_color == image[row][col]): 
                return
            
            visited.add((row, col))
            image[row][col] = change
            
            for r_change, c_change in directions:
                dfs(row + r_change, col + c_change, source_color, change)
        
        initial = image[sr][sc]
        dfs(sr, sc, initial, color)
        
        return image