class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 0
        
        for indx in range(n):
            nums[indx] += prefix
            prefix = nums[indx]
        
        return nums