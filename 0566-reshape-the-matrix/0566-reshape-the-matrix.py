class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        new_mat = [[0]*c for _ in range(r)]
        
        for row in range(m):
            for col in range(n):
                i = row*n + col
                newRow = i//c
                newCol = i%c
                new_mat[newRow][newCol] = mat[row][col]
        
        return new_mat
                
                
        