class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        mod = 10**9 + 7
        dp = [[0]*(k + 1) for num in range(n + 1)]
        
        
        for num in range(1, n + 1):
            for indx in range(k + 1):
                if not indx:
                    dp[num][indx] = 1
                else:
                    temp = (dp[num - 1][indx] - (dp[num - 1][indx - num] if indx - num >= 0 else 0))%mod
                    dp[num][indx] = (dp[num][indx - 1] + temp)%mod

        return (dp[n][k] - (dp[n][k - 1] if k > 0 else 0))%mod
                
                    
        