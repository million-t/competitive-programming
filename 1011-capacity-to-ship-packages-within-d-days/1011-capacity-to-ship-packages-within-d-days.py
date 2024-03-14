class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        
        def check(x):
            
            
            cur_sum = 0
            days_count = 1
            
            for weight in weights:
                cur_sum += weight
                
                if cur_sum > x:
                    days_count += 1
                    cur_sum = weight
                    
                    if days_count > days:
                        return False
            
            return days_count <= days
                
        
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = low + (high - low)//2
            
            if check(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        
        return low