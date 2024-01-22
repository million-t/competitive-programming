class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        index = 0
        
        
        while index < length:    
            target_ind = nums[index] - 1
            
            if target_ind != index and nums[target_ind] != nums[index]:
                nums[target_ind], nums[index] = nums[index], nums[target_ind]
            
            else:
                index += 1
        
        
        for ind, num in enumerate(nums):
            if num - 1 != ind:
                return [num, ind + 1]
            
            