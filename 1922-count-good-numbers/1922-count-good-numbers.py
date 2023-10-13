class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        
        mod = 10**9 + 7
        _pow = n//2 
        if not n & 1:
            return (pow(5, _pow, mod)*pow(4, _pow, mod))%mod
        
        else:
            return (pow(5, _pow + 1, mod)*pow(4, _pow, mod))%mod
            
        