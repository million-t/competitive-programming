class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        pref_ones = 0
        dp = [0]*(len(s) + 1)
        ops = 0
        
        for ind, bit in enumerate(s):
            
            if bit == '1':
                if pref_ones != ind:
                    ops = max(ops, dp[ind - 1] + ind - pref_ones)
                    dp[ind] += dp[ind - 1] + 1
            
                pref_ones += 1
            
            else:
                dp[ind] = max(dp[ind - 1] - 1, 0)
        
        
        return ops
                