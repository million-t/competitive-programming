class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        index = 0
        
        
        while index < length:
            
            target_ind = nums[index] - 1
            
            if target_ind != index and nums[target_ind] != nums[index]:
                nums[target_ind], nums[index] = nums[index], nums[target_ind]
            
            else:
                index += 1
        
        
        duplicates = []
        
        for ind, num in enumerate(nums):
            if num - 1 != ind:
                duplicates.append(num)
        
        return duplicates
        