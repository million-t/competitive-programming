class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        
        dp = [1]*len(nums)
        
        for indx, num in enumerate(nums):
            for prev_indx in range(indx):
                
                if nums[prev_indx] < num:
                    dp[indx] = max(dp[indx], dp[prev_indx] + 1)
                    
        
        return max(dp)
        
        
        
        
#         @cache
#         def dp(indx, prev):
            
#             if indx < 0:
#                 return 0
            
#             cur_max_len = dp(indx - 1, prev)
#             if nums[indx] < prev:
#                 return max(cur_max_len, dp(indx - 1, nums[indx]) + 1)
            
#             return cur_max_len
        
#         return dp(len(nums) - 1, float('inf'))
                
        