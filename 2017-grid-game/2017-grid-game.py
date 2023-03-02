class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        row1, row2 = grid
        
        top_suffix = sum(row1)
        bottom_prefix = 0
        sec_bot_score = float('inf')
        
        for i in range(n):
            top_suffix -= row1[i]
            
            sec_bot_score = min(sec_bot_score, max(bottom_prefix, top_suffix))
            bottom_prefix += row2[i]
            
        return sec_bot_score
        
        
        
        