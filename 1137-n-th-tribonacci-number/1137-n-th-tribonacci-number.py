class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n < 3:
            return int(n > 0)
        
        a, b, c = 0, 1, 1
        ans = 2
        
        for num in range(3, n + 1):
            
            ans = a + b + c
            a = b
            b = c
            c = ans
        
        
        return ans
        
        