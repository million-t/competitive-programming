class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def helper(row1, col1, row2, col2):
            
            return prefix_sum[row2 + 1][col2 + 1] - prefix_sum[row2 + 1][col1] - prefix_sum[row1][col2 + 1] + prefix_sum[row1][col1]
        
        
        
        rows = len(mat)
        cols = len(mat[0])
        
        prefix_sum = [[0]*(cols + 1) for _ in range(rows + 1)]
        
        for row in range(rows):
            for col in range(cols):
                prefix_sum[row + 1][col + 1] = prefix_sum[row][col + 1] + prefix_sum[row + 1][col] - prefix_sum[row][col] + mat[row][col]
                
        
        res = [[0]*cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                res[r][c] = helper(max(0, r - k), max(0, c - k), min(rows - 1, r + k), min(cols - 1, c + k))
            
        
        return res