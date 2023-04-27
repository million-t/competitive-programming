class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        
        def inbounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1)
        ]
        
        ROWS, COLS = len(grid), len(grid[0])
        
        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        
        while queue:
            row, col, path_len = queue.popleft()
            
            if (row, col) == (ROWS - 1, COLS - 1):
                return path_len
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if inbounds(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, path_len + 1))
        
        return -1
            
        