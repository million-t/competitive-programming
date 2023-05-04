class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        
        def inbound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        
        start = None
        for _row in range(ROWS):
            for _col in range(COLS):
                
                if grid[_row][_col]:
                    start = (_row, _col)
                    break
            
            if start:
                break
        
        visited = set([start])
        queue = deque()
        
        
        stack = [(start)]
        while stack:
            row, col = stack.pop()
            
            queue.append((row, col))
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc]:
                    stack.append((nr, nc))
                    visited.add((nr, nc))
                    
        flips = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        if grid[nr][nc]:
                            return flips
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
                        
                    
            
            flips += 1
                
                
                
                
                
                
                
            
        
        
        
        
            