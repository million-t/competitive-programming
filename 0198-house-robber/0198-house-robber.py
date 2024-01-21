class Solution:
    def rob(self, nums: List[int]) -> int:
        
        size = len(nums)
        if size < 2:
            return max(nums)
        
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for ind in range(2, size):
            dp[ind] = max(dp[ind - 1], dp[ind - 2] + nums[ind])
        
        return max(dp[-1], dp[-2])
                
        