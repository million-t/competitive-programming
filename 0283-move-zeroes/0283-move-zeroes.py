class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        
        for seeker in range(len(nums)):
            
            if nums[seeker] != 0:
                
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            
            