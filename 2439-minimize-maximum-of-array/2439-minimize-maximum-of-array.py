class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        ans = 0
        pref = 0
        
        for indx in range(len(nums)):
            pref += nums[indx]
            ans = max(ans, ceil(pref/(indx + 1)))
        
        return ans
        
        
        