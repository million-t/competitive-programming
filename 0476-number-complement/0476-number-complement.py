class Solution:
    def findComplement(self, num: int) -> int:
        
        temp = num
        complement = 0
        
        while num:
            complement <<= 1
            complement |= 1
            num >>= 1
            
        
        return complement^temp
        