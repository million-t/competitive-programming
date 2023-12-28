class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.mod = 10**9 + 7
        
        @cache
        def dp(n, k, t):
            if n == 1:
                if 0 < t <= k:
                    return 1
                
                return 0
            
            ans = 0
            for i in range(1, min(k + 1, t + 1)):
                ans += dp(n - 1, k, t - i)
                ans %= self.mod
                
            return ans
        
        
        
        return dp(n, k, target)
        