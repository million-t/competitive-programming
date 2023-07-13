class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n + 1)
        dp[0] = dp[1] = 1
        
        for nodes in range(2, n + 1):
            for ind in range(nodes//2):
                dp[nodes] += dp[ind]*dp[nodes - ind - 1]
            
            dp[nodes] *= 2
            if nodes%2:
                dp[nodes] += dp[nodes//2]**2
            
        
        return dp[-1]