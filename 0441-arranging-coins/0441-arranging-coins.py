class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        start = 1
        end = n
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            mid_sum = mid*(mid + 1)//2
            
            if mid_sum <= n:
                start = mid + 1
            
            else:
                end = mid - 1
        
        return start - 1
        
        
        