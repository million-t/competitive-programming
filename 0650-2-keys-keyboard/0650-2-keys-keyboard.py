class Solution:
    def minSteps(self, n: int) -> int:
        
        def factorize(num):
            
            factors = []
            for ind in range(2, num + 1):
                
                 while num > 1 and not num%ind:
                    num //= ind
                    factors.append(ind)
                        
            
            return factors
        
        return sum(factorize(n))
        