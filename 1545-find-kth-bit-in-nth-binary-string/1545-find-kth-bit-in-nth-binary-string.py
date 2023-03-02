class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1
        mid = 2**(n-1)
        
        if k == 1 or n == 1:
            return '0'
        
        if k == mid:
            return '1'
        
        if k < mid:
            return self.findKthBit(n - 1, k)
    
        return '0' if self.findKthBit( n - 1, length - k + 1 ) == '1' else '1'
        
        
        