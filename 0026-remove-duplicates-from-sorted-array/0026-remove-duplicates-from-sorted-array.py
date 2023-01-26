class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, k = 1,  1
        
        for right in range(1, len(nums)):
            
            if nums[right]!=nums[right-1]:
                nums[left] = nums[right]
                
                left += 1
                k += 1
                
        return k