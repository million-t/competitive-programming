class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        seenRow, seenCol = set(), set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    seenRow.add(row)
                    seenCol.add(col)
                    
        for row in seenRow:
            for col in range(n):
                matrix[row][col] = 0
        
        for col in seenCol:
            for row in range(m):
                matrix[row][col] = 0