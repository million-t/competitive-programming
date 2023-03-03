class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # length = 2**(n-1)
        # mid = length/2
        
        mid = 2**(n-2)
        
        if n == 1:
            return 0
                
        if k > mid:
            interm = self.kthGrammar(n - 1, k - mid)
            
            if interm == 1: return 0
            return 1
        
        return self.kthGrammar(n - 1, k)