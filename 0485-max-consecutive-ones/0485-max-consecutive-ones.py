class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_len = 0
        cur_sum = 0
        left = 0
        
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while left <= right and cur_sum != right - left + 1:
                cur_sum -= nums[left]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len