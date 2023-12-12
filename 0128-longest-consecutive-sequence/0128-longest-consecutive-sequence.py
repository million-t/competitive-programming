class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        
        @cache
        def dp(num):
            if num not in seen:
                return 0
            return dp(num + 1) + 1
        
        
        ans = 0
        for num in nums:
            ans = max(ans, dp(num))
        
        return ans