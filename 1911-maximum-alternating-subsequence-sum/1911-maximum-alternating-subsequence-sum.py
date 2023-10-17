class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        
        even = 0
        odd = 0
        
        for num in nums:
            even = max(even, num + odd)
            odd = max(odd, even - num)
        
        return even