class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        def inbound(row, col, n):
            return 0 <= row < n and 0 <= col < n
        
        length = len(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        queue = deque()
        seen = set()
        zeros = 0
        
        for row in range(length):
            for col in range(length):
                if grid[row][col]:
                    queue.append((row, col))
                    seen.add((row, col))
                
                else:
                    zeros += 1
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    if inbound(nr, nc, length) and (nr, nc) not in seen:
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            
            dist += 1
        
        
        return dist - 1 if zeros else -1