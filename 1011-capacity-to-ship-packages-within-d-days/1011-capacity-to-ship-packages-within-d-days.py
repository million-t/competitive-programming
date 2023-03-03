class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def findDays(n):
            
            sum_so_far = weights[0]
            days_count = 1
            
            for i in range(1, len(weights)):
                if sum_so_far + weights[i] > n:
                    sum_so_far = 0
                    days_count += 1
                
                sum_so_far += weights[i]

            return days_count
        
        
        
        start = max(weights)
        end = sum(weights)
        
        
        while start <= end:
            mid = start + (end - start)//2
            
            temp = findDays(mid)
            if temp <= days:
                end = mid - 1   
            
            else:
                start = mid + 1
        
        return start
            
                
        