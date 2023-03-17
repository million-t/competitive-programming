class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        start = 0
        end = rows*columns - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            _row = mid//columns
            _col = mid%columns
            
            cur_num = matrix[_row][_col]
            
            if cur_num == target:
                return True
            
            elif cur_num > target:
                end = mid - 1
            
            else:
                start = mid + 1
        
        
        return False
        