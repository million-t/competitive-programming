class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        
        dp = [defaultdict(int) for _ in range(len(nums))]
        count = 0
        
        for ind, num in enumerate(nums):
            for sec_ind in range(ind):
                dif = num - nums[sec_ind]
                dp[ind][dif] += dp[sec_ind][dif] + 1
                count += dp[sec_ind][dif]
        
        return count
        