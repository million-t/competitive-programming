class Solution:
    
    def primes_in_the_range(self, left, n):
        
        if n < 2: 
            return []
        
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False
        
        limit = int(sqrt(n))
        
        for num in range(2, limit + 1):
            
            if is_prime[num]:
                
                for multiple in range(num*num, n, num):
                    is_prime[multiple] = False
        
        return [num for num, prime in enumerate(is_prime) if prime and num >= left]
                
        
        
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes = self.primes_in_the_range(left, right + 1)
        pairs = [float('-inf'), float('inf')]
        
        for index in range(1, len(primes)):
            if primes[index] - primes[index - 1] < pairs[1] - pairs[0]:
                pairs[0] = primes[index - 1]
                pairs[1] = primes[index]
            
        
        if pairs[0] == float('-inf'):
            pairs = [-1, -1]
        
        return pairs
            
        
        