class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        nums_size = len(nums)
        for indx in range(nums_size):
            right_sum -= nums[indx]
            
            if left_sum == right_sum:
                return indx
            
            left_sum += nums[indx]
            
        return -1
                
        