class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        tower = [[0]*(row + 1) for row in range(query_row + 1)]
        tower[0][0] = poured
        
        for row in range(1, query_row + 1):
            for col in range(row + 1):
                
                if col > 0 and tower[row - 1][col - 1] > 1:
                    tower[row][col] += (tower[row - 1][col - 1] - 1)/2
                
                if col < row and tower[row - 1][col] > 1:
                    tower[row][col] += (tower[row - 1][col] - 1)/2
        
        ans = tower[query_row][query_glass]
        return ans if ans <= 1 else 1 
                
            
                
        