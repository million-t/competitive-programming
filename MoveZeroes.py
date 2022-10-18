class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 1: return nums
        l, r = 0, 1
        while l< r and r < N:
            if nums[l] == 0:
                while r<N-1 and nums[r]==0:
                    r += 1
                nums[l], nums[r] = nums[r],nums[l]
            r+=1
            l += 1
            
