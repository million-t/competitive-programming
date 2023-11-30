class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
        ans = 0
        while n:
            num = n&(-n)
            n ^= num
            ans = 2*num - ans - 1
            
        return ans
        