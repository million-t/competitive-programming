class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        ans = nums[0]
        pref = nums[0]
        
        for indx in range(1, len(nums)):
            pref += nums[indx]
            ans = max(ans, ceil(pref/(indx + 1)))
        
        return ans
        
        
        