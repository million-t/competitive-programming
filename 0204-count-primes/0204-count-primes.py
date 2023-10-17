class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return 0
        
        is_prime = [1]*n
        is_prime[0] = is_prime[1] = 0
        
        limit = n**(0.5)
        num = 2
        
        while num <= limit:
            
            if not is_prime[num]:
                num += 1
                continue

            sieve = num*num
            while sieve < n:
                is_prime[sieve] = 0
                sieve += num
            
            num += 1
        
        return sum(is_prime)