class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        bit_diff = x^y
        ans = 0
        
        while bit_diff:
            ans += bit_diff&1 
            bit_diff >>= 1
            
        return ans