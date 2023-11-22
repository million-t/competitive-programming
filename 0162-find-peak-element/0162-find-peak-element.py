class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            if 0 < mid < len(nums) - 1 and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                start = mid + 1
            
            else:
                end = mid - 1
            
            
        return start
        
        