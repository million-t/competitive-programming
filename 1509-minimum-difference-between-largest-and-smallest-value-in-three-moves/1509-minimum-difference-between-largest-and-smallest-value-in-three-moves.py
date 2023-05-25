class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        nums.sort()
        
        left = 0
        min_range = float('inf')
        
        for right in range(len(nums) - 4, len(nums)):
            min_range = min(min_range, nums[right] - nums[left])
            left += 1
        
        return min_range
            
        