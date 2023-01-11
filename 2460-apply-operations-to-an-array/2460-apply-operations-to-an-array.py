class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1
        
        
        write = 0
        for read in range(len(nums)):
            if nums[read]:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write += 1
        return nums
        
        
        