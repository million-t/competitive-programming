class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        square = [0]*length
        
        left = 0
        right = length - 1
        
                
        for write_index in range(right, -1, -1):
            
            left_sqr = nums[left]*nums[left]
            right_sqr = nums[right]*nums[right]
            
            if right_sqr >= left_sqr:
                square[write_index] = right_sqr
                right -= 1
            
            else:
                square[write_index] = left_sqr
                left += 1
                
        
        return square