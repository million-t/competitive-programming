class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        inc = True
        for ind in range(1, len(nums)):
            if nums[ind] < nums[ind - 1]:
                inc = False
                break
        
        dec = True
        for ind in range(1, len(nums)):
            if nums[ind] > nums[ind - 1]:
                dec = False
                break
        
        return inc or dec
        