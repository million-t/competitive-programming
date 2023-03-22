class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        length = len(nums)
        ind = 0 
        
        
        while ind < length:
            
            right_place = nums[ind] - 1
            if 0 <= right_place < length and right_place != ind and nums[ind] != nums[right_place]:
                nums[right_place], nums[ind] = nums[ind], nums[right_place]
            
            else:
                ind += 1
        
        
        for ind, num in enumerate(nums):
            if num - 1 != ind:
                return ind + 1
        
        return nums[-1] + 1
        
        
        
        
        