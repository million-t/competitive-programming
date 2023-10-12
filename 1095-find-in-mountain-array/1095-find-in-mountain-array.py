# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        start = 0
        end = mountain_arr.length() - 1
        
        while start <= end:
            
            mid = start + (end - start)//2
            if mid < mountain_arr.length() - 1 and mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                start = mid + 1
            
            else:
                end = mid - 1
        
        low, high = 0, start
        while low <= high:
            mid = low + (high - low)//2

            if mountain_arr.get(mid) < target:
                low = mid + 1
            else:                
                high = mid - 1
        
        if mountain_arr.get(low) == target:
            return low
        
        low, high = start, mountain_arr.length() - 1
        while low <= high:
            mid = low + (high - low)//2

            if mountain_arr.get(mid) <= target:
                high = mid - 1
            else:                
                low = mid + 1
            
        if low <= mountain_arr.length() - 1 and mountain_arr.get(low) == target:
            return low
        
        return -1
        
            
            
        
        