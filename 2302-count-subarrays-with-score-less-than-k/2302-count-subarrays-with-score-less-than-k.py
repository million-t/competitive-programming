class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        ans = 0
        cur_sum = 0
        left = 0
        
        for right, num in enumerate(nums):
            cur_sum += num
            while left <= right and cur_sum*(right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1
            
            ans += right - left + 1
        
        return ans
            