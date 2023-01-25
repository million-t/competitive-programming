class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size  = len(nums)
        k = k%size
        
        def reverseArr(left, right):
            
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        
        reverseArr(0, size - 1)
        reverseArr(0, k - 1)
        reverseArr(k, size - 1)