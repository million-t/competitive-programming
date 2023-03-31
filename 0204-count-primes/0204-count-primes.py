class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2: return 0
        
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False
        
        num = 2
        bound = n**(1/2)
        
        while num <= bound:
            
            if is_prime[num]:
                
                sieve = num*num
                
                while sieve < n:
                    is_prime[sieve] = False
                    sieve += num
                
            num += 1
        
        
        
        primes = 0
        
        for val in is_prime:    
            primes += val
        
        return primes