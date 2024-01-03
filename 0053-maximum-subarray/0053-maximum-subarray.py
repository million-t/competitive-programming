class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = float('-inf')
        prev = 0
        
        for num in nums:
            prev = max(num, prev + num)
            ans = max(ans, prev)
        
        return ans
        
        
        