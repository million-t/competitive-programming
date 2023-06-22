class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def backtrack(ind, cur_target, target):
            
            key = (ind, cur_target, target)
            if key in memo:
                return memo[key]
            
            if ind >= len(nums):
                memo[key] = int(cur_target == target) 
                return memo[key]
            
            neg = backtrack(ind + 1, cur_target - nums[ind], target)
            pos = backtrack(ind + 1, cur_target + nums[ind], target)
            
            memo[key] = neg + pos
            return memo[key]
    
        
        return backtrack(0, 0, target)
            
        