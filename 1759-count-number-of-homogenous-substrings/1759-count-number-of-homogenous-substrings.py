class Solution:
    def countHomogenous(self, s: str) -> int:
        
        ans = 0
        left = 0
        mod = 10**9 + 7
        
        for right, char in enumerate(s):
            if s[left] != char:
                n = right - left
                val = n*(n + 1)//2
                ans += val
                ans %= mod
                left = right
        
        n = len(s) - left
        ans += n*(n + 1)//2
        return ans % mod
        
        
                    
                    
                
        