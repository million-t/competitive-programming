class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left = 0
        
        for right in range(len(nums)):
            if not nums[right]&1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
        