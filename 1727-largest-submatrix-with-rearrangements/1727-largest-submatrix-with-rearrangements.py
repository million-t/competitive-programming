class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] and row:
                    matrix[row][col] += matrix[row - 1][col]
        
        ans = 0
        for row in range(rows):
            matrix[row].sort(reverse = True)
            for col, val in enumerate(matrix[row]):
                ans = max(ans, matrix[row][col]*(col + 1))
        
        return ans