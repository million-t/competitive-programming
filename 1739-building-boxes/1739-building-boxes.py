class Solution:
    
    def findNearestSum(self, num):
        
        low = 1
        high = num
        
        while low <= high:
            mid = low + (high - low)//2
            temp = mid*(mid + 1)//2
            if temp > num:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return high, high*(high + 1)//2
    
    
    def minimumBoxes(self, n: int) -> int:
        
        
        def computeCover(m):
            temp = (m*(m + 1)*(2*m + 1))//6 + m*m - (m*(m - 1)//2)
            return temp//2
        
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low)//2
            n1, _sum = self.findNearestSum(mid)
            cur = computeCover(n1)
            left = mid - _sum
            
            additional = left*(left + 1)//2
            
            
                        
            if cur + additional >= n:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low
            
        
        
            
            