class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        
        return n.bit_count() == 1
        