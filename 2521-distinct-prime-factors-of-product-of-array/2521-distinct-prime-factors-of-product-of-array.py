class Solution:
    
    def primes_less_than(self, n):
        if n < 2: return []
        
        is_prime = [1]*n
        is_prime[0] = is_prime[1] = 0
        
        num = 2
        bound = n**(1/2)
        
        while num <= bound:
            
            if is_prime[num]:
                
                sieve = num*num
                
                while sieve < n:
                    is_prime[sieve] = 0
                    sieve += num
                
            num += 1
        
        return [index for index, prime in enumerate(is_prime) if prime]
    
    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        
        primes = self.primes_less_than(1000)   
    
        
        def factorize(num):
            
            factors = set()
            ind = 0
            
            while num > 1 and ind < len(primes):
                 while ind < len(primes) and num > 1 and not num%primes[ind]:
                    num //= primes[ind]
                    factors.add(primes[ind])
                
                 ind += 1
            
            return factors
        
        
        
        
        factors_array = [factorize(num) for num in nums]
        
        unique_primes = set()
        for _set in factors_array:
            unique_primes = unique_primes.union(_set)
        
        return len(unique_primes)