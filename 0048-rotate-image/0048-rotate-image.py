class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(n):
            for col in range(n//2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]
        