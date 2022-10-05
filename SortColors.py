class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        whiteStartIndex, blueStartIndex, whiteDetected = 0, 0, False
        for i in range(len(nums)):
            if nums[i] == 0:
                if whiteDetected:
                    nums[i] = nums[blueStartIndex]
                    nums[blueStartIndex] = 1
                else:
                    nums[i] = nums[whiteStartIndex]
                nums[whiteStartIndex] = 0
                whiteStartIndex += 1
                blueStartIndex +=1
            elif nums[i] == 1:
                whiteDetected = True
                nums[i] = nums[blueStartIndex]
                nums[blueStartIndex] = 1
                blueStartIndex += 1
            
