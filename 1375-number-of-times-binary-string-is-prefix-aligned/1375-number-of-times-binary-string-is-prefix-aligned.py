class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        pa = 0
        before = 0
        after = 0
        temp = [0]*len(flips)
        
        for indx, flip in enumerate(flips):
            if temp[indx]:
                after -= 1
                before += 1
            
            temp[flip - 1] = 1
            if flip - 1 <= indx:
                before += 1
            
            else:
                after += 1
            
            if before == indx + 1 and not after:
                pa += 1
        
        return pa
                
            
            
        
        