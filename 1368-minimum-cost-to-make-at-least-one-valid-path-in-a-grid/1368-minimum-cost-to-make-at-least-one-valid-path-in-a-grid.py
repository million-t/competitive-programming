class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def inbound(r, c):  return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        rows, cols = len(grid), len(grid[0])
        costs = [[float("inf")]*cols for _ in range(rows)]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0)]
        
        while heap:
            cost, row, col = heappop(heap)
            
            if cost >= costs[row][col]:
                continue
            
            costs[row][col] = cost
            for indx, (dr, dc) in enumerate(moves):
                nr, nc = row + dr, col + dc
                if not inbound(nr, nc):
                    continue
                    
                if indx + 1 == grid[row][col]:
                    heappush(heap, (cost, nr, nc))
                
                else:
                    heappush(heap, (cost + 1, nr, nc))
        
        return costs[-1][-1]