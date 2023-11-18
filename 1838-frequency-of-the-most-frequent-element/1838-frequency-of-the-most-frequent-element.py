class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0
        ops = 0
        ans = 1
        
        for right in range(1, len(nums)):
            ops += (nums[right] - nums[right - 1])*(right - left)
            
            while ops > k:
                ops -= nums[right] - nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
        