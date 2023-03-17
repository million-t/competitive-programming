class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def findHrsNeeded(pile):
            
            hrs = 0
            for num in piles:
                hrs += ceil(num/pile)
            
            return hrs
            
        
        start = 1
        end = max(piles)
        
        while start <= end:
            
            mid = start + (end - start)//2
            cur_hrs = findHrsNeeded(mid)
            
            if cur_hrs > h:
                start = mid + 1
            
            else:
                end = mid - 1
            
        
        return start
            
            
        