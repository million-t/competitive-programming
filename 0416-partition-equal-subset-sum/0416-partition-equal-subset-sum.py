class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        LENGTH = len(nums)
        
        memo = {}
        
        def dp(index, target):
            
            if index >= LENGTH or target <= 0:
                return target == 0
            
            
            state = (index, target)
            if state not in memo:
                memo[state] = dp(index + 1, target - nums[index]) or dp(index + 1, target)
            
            return memo[state]
        
        _sum = sum(nums)
        target = _sum//2
        return (not _sum%2) and dp(0, target)