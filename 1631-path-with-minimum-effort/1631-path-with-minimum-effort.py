class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbounds(row, col): return 0 <= row < len(heights) and 0 <= col < len(heights[0]) 
        
        
        heap = [(0, 0, 0)]
        visited = set()
        tar_row, tar_col = len(heights) - 1, len(heights[0]) - 1
        
        
        while heap:
            effort, row, col = heappop(heap)
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            
            if row == tar_row and col == tar_col:
                return effort
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if inbounds(new_row, new_col):
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    heappush(heap, (new_effort, new_row, new_col))

            
        