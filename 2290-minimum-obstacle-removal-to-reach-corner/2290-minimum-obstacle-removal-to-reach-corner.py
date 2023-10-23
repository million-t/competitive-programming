class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        def inbounds(row, col): return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        m, n = len(grid), len(grid[0])
        target = (m - 1, n - 1)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        heap = [(0, 0, 0)]
        visited = set()
        
        while heap:
            removed, row, col = heappop(heap)
            
            if (row, col) == target:
                return removed
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if inbounds(nr, nc):
                    heappush(heap, (removed + grid[nr][nc], nr, nc))
        
        