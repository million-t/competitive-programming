class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        
        @cache
        def dp(indx, _max, k):
            
            if indx == n:
                if k == 0:
                    return 1
                
                return 0
            
            ans = 0
            
            for num in range(1, _max + 1):
                ans += dp(indx + 1, _max, k)
                ans %= MOD
            
            for num in range(_max + 1, m + 1):
                ans += dp(indx + 1, num, k - 1)
                ans %= MOD
                
            return ans
        
        return dp(0, 0, k)