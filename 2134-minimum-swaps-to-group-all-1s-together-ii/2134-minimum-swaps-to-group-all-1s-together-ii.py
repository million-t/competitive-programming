class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = sum(nums)
        if not ones:
            return 0
        
        nums += nums
        ans = float('inf')
        seen = left = 0
        
        for right, bit in enumerate(nums):
            seen += bit       
            if right - left + 1 == ones:
                ans = min(ans, ones - seen)
                seen -= nums[left]
                left += 1
        
        return ans
        
        