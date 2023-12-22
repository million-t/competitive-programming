class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        
        max_ = -1
        count = ans = 0 
        
        for indx, num in enumerate(flips):
            
            max_ = max(num, max_)
            count += 1
            
            if count == max_:
                ans += 1
        
        return ans
            