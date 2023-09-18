class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        dp = [num for num in range(n + 1)]
        
        
        for num in range(2, n + 1):
            
            for factor in range(2, int(num**0.5) + 1):
                if not num%factor:
                    dp[num] = min(dp[num], dp[factor] + dp[num//factor])
        
        return dp[-1]
        