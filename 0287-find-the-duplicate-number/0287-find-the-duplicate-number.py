class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        length = len(nums)
        index = 0
        
        while index < length:
            target_ind = nums[index] - 1
            
            if target_ind != index:
                if nums[target_ind] == nums[index]:
                    return nums[index] 
                
                nums[target_ind], nums[index] = nums[index], nums[target_ind]
            
            else:
                index += 1
        
        