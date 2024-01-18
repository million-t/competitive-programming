class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        size = len(nums)
        nums.sort()
        ans = 0
        
        for third in range(2, size):
            sec = third
            
            for first in range(third - 1):
                while first < sec - 1 and nums[first] + nums[sec - 1] > nums[third]:
                    sec -= 1
                
                if nums[first] + nums[sec] > nums[third]:
                    ans += third - max(first + 1, sec)
        
        return ans
            
        