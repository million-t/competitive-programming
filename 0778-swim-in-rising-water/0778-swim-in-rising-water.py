class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def inbound(row, col): return 0 <= row < len(grid) and 0 <= col < len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(candidate):
            if grid[0][0] > candidate:
                return False
            
            target_r, target_c  = len(grid) - 1, len(grid[0]) - 1
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            
            while queue:
                row, col = queue.popleft()
                
                if (row, col) == (target_r, target_c):
                    return True
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] <= candidate:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                
            return False
    
        
        start = 0
        end = n*n
        
        while start <= end:
            
            mid = start + (end - start)//2
            temp = bfs(mid)
            if temp:
                end = mid - 1
            
            else:
                start = mid + 1
        
        return start
                
                        
        