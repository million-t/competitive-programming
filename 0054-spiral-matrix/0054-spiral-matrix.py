class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = n
        top = 0
        bottom = m
        
        arr = []
        while top<bottom and left<right:
            for curCol in range(left, right):
                arr.append(matrix[top][curCol])
            top += 1
            for curRow in range(top, bottom):
                arr.append(matrix[curRow][right - 1])
            right -= 1
            
            if left>=right or top>=bottom:
                break
            
            for curCol in range(right - 1, left - 1, - 1):
                arr.append(matrix[bottom - 1][curCol])
            bottom -= 1
            for curRow in range(bottom - 1, top - 1, -1):
                arr.append(matrix[curRow][left])
            left += 1
        
        return arr                
            
            
        
        