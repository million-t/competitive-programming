class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1 
        midPoint = 0
        
        while start <= end:
            midPoint = start + (end - start)//2
            
            if nums[midPoint] == target:
                return midPoint

            elif start == end and nums[midPoint] < target:
                return midPoint + 1

            elif nums[midPoint] < target:
                start = midPoint + 1
            
            elif nums[midPoint] > target:
                end = midPoint - 1
            
        return midPoint