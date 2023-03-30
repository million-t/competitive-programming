class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        left_bit = n&1
        
        
        while n:
            
            n >>= 1
            
            if left_bit == n&1:
                return False
            
            left_bit = n&1
        
        return True
            
            
        