class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        
        left, right = 0, n
        top, bottom = 0, n
        
        val = 1
        while top<bottom and left<right:
            for curCol in range(left, right):
                mat[top][curCol] = val
                val+=1
            top += 1
            
            for curRow in range(top, bottom):
                mat[curRow][right - 1] = val
                val += 1
            right -= 1
            
            if left>=right or top>=bottom:
                break
            
            for curCol in range(right - 1, left - 1, - 1):
                mat[bottom - 1][curCol] = val 
                val += 1 
            bottom -= 1
            
            for curRow in range(bottom - 1, top - 1, -1):
                mat[curRow][left] = val
                val += 1
            left += 1
            
        return mat