class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for index in range(len(nums)):
            
            while nums[index] != index + 1 and nums[index]:
                
                right_place = nums[index] - 1
                nums[index], nums[right_place] = nums[right_place], nums[index]
            
        try:
            return nums.index(0) + 1
        
        except:
            return 0
            
            
        