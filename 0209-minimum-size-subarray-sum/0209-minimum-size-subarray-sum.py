class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        min_len = float('inf')
        
        left = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while cur_sum - nums[left] >= target:
                cur_sum -= nums[left]
                left += 1
            
            if cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                
        
        return min_len if min_len != float('inf') else 0 
            