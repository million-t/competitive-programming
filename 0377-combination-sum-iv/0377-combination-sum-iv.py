class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0]*(target + 1)
        for num in nums:
            if num <= target:
                dp[num] += 1
        
        for ind in range(target + 1):
            for num in nums:
                if num + ind <= target:
                    dp[num + ind] += dp[ind]
        
        return dp[-1]
        