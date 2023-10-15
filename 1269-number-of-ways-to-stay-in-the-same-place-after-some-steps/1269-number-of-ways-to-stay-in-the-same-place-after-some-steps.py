class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        
        mod = 10**9 + 7
        dp = [defaultdict(int) for step in range(steps + 1)]
        dp[0][0] += 1
        
        for step in range(1, steps + 1):
            for indx in range(min(steps + 1, arrLen)):
                dp[step][indx] = dp[step - 1][indx - 1] + dp[step - 1][indx] + dp[step - 1][indx + 1]
                dp[step][indx] %= mod

        return dp[-1][0]
            