class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m*n - 1
        
        while start <= end:
            mid = (start + end)//2
            
            col = mid%n
            row = mid//n
            
            num = matrix[row][col]
            if num == target:
                return True
            elif num < target:
                start = mid + 1
            elif num > target:
                end = mid - 1
                
        return False
            
        