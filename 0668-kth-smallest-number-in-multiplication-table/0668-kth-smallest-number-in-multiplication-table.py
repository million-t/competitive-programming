class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def check(mid):
            
            row_lim = min(m, mid)
            count = 0
            
            for row in range(1, row_lim + 1):
                count += min(n, (mid - 1)//row)
            
            return count
        
        
        
        start = 1
        end = m*n
        
        
        while start <= end:
            mid = start + (end - start)//2
            
            
            count = check(mid)
            if count < k:
                start = mid + 1
            
            else:
                end = mid - 1
        
        return start - 1