class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*(n + 1) for _ in range(n + 1)]
        
        for r1, c1, r2, c2 in queries:
            matrix[r1][c1] += 1
            matrix[r2 + 1][c2 + 1] += 1
            matrix[r2 + 1][c1] -= 1
            matrix[r1][c2 + 1] -= 1
            
        
        for col in range(n + 1):
            for row in range(1, n + 1):
                matrix[row][col] += matrix[row - 1][col]
                
        for row in range(n + 1):
            for col in range(1, n + 1):
                matrix[row][col] += matrix[row][col - 1]
        
        
        
        for i, row in enumerate(matrix):
            matrix[i] = row[:-1]
        
        matrix.pop()
        return matrix
            
                
        
            
                 
        