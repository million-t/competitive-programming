class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        
        target = length - 1
        
        for index in range(length - 1, -1, -1):
            if index + nums[index] >= target:
                target = index
        
        return not target 