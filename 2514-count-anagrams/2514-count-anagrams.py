class Solution:
    
    def multiply(self, a, b, m):
        return ((a % m) * (b % m)) % m
    
    def binary_exponentiation(self, base, exponent, mod):
        
        result = 1
        while exponent > 0:
            if exponent & 1:
                result = self.multiply(base, result, mod)
                
            base = self.multiply(base, base, mod)
            exponent >>= 1
            
        return result
    
    def inverse(self, a, mod):
        return self.binary_exponentiation(a, mod - 2, mod)
    
    def division(self, a, b, mod):
        return self.multiply(a, self.inverse(b, mod), mod)
    
    
    def countAnagrams(self, s: str) -> int:
        
        mod = 10**9 + 7
        words = s.split()
        max_perm_val = max([len(word) for word in words])
        
        
        ans = 1
        for word in words:
            count = Counter(word)
            temp = factorial(len(word))%mod
            
            for freq in count.values():
                temp = self.division(temp, factorial(freq), mod)
            
            ans *= temp
            ans %= mod
        
        return ans