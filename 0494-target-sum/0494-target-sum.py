class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def backtrack(ind, cur_target, target):
            
            if ind >= len(nums):
                return int(cur_target == target)
            
            neg = backtrack(ind + 1, cur_target - nums[ind], target)
            pos = backtrack(ind + 1, cur_target + nums[ind], target)
            
            return neg + pos
    
        
        return backtrack(0, 0, target)
            
        