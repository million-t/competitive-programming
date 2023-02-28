class Solution:
    def __init__(self):
        self.computed = {0:0, 1:1} 
    
    def fib(self, n: int) -> int:
        if n in self.computed: 
            return self.computed[n]
        
        prev1 = self.fib(n-2)
        prev2 = self.fib(n-1)
        
        self.computed[n] = prev1 + prev2
        
        return self.computed[n] 
        