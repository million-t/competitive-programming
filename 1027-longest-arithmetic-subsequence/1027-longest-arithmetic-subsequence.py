class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        length = len(nums)
        dp = defaultdict(lambda: defaultdict(lambda: 1))
        
        for ind in range(length):
            num = nums[ind]
            for j in range(ind):
                prev = nums[j]
                dp[ind][num - prev] = max(dp[ind][num - prev], dp[j][num - prev] + 1)
        
        ans = 0
        for ind in dp.values():
            for val in ind:
                ans = max(ans, ind[val])
        
        return ans
        
        
        
        
        