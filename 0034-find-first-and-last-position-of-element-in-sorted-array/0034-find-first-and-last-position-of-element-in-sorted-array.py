class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums) - 1
        
        mid = start + (end - start)//2
        
        while start < end:
            if nums[mid] >= target:
                end = mid
            
            else:
                start = mid + 1
        
            mid = start + (end - start)//2
        
        first = mid 
        
        #============================================
        if nums and nums[mid] != target:
            return [-1, -1]
        #============================================
        start = first 
        end = len(nums) - 1
        
        mid = start + (end - start)//2
        
        while nums and start <= end:
            if nums[mid] <= target:
                start = mid + 1               
            
            else:
                end = mid - 1
        
            mid = start + (end - start)//2
        
        last = mid 
    
        return [first, last]