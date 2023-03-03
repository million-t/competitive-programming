# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 1
        high = n
        
        mid = low + (high - low)//2
        
        while low < high:
            
            if isBadVersion(mid):
                high = mid
            
            else:
                low = mid + 1
            
            mid = low + (high - low)//2
        
        return mid
        