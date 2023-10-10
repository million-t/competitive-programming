class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        
        length = len(nums)
        ans = len(nums)
        nums = sorted(set(nums))
        
        for left in range(len(nums)):
            target = length + nums[left] - 1
            right = bisect_right(nums, target)
            ans = min(ans, left + length - right)    
        
        return ans