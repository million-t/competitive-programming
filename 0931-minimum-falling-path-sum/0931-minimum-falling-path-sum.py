class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS):
                
                _min = matrix[row + 1][col] 
                if col > 0:
                    _min = min(_min, matrix[row + 1][col - 1])
                
                if col < COLS - 1:
                    _min = min(_min, matrix[row + 1][col + 1])
                
                matrix[row][col] += _min
        
        return min(matrix[0])
                    
            
        