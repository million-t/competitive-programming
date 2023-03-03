class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        
        low, high = 0, x//2
        mid = low + (high - low)//2
        
        while low <= high:
                
            if mid*mid < x:
                low = mid + 1
            
            elif mid*mid > x:
                high = mid - 1
            
            else:
                return mid
            
            mid = low + (high - low)//2
        
        return mid
        