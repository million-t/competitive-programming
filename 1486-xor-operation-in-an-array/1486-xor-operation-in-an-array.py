class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        for ind in range(n):
            ans ^= (start + 2*ind)
        
        return ans
        
        