class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        ans = 0
        neg = 0
        pos = 0
        
        for num in nums:
            neg = min(neg + num, num)
            pos = max(pos + num, num)
            ans = max(ans, pos, abs(neg))
        
        return ans
        
        