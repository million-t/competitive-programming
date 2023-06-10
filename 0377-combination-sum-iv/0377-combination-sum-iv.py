class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0]*(target + 1)
        dp[0] = 1
        
        for interm in range(target):
            
            for num in nums:
                if interm + num > target:
                    continue
                
                dp[interm + num] += dp[interm]
        
        # print(dp)
        return dp[target]
        