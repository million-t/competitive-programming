class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def findHours(n):
            
            hrs = 0
            
            for pile in piles:
                if pile > n:
                    hrs += ceil(pile/n)
                
                else:
                    hrs += 1
            
            return hrs
        
        
        start = 1
        end = max(piles)
        
        while start <= end:
            mid = start + (end - start)//2
            
            cur_hr = findHours(mid)
            
            if cur_hr <= h:
                end = mid - 1
            
            else:
                start = mid + 1
            
        return start