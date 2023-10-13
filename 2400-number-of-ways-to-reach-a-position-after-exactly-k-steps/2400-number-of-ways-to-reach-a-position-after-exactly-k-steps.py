class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        _min = startPos - k
        _max = startPos + k
        mod = 10**9 + 7
        
        dp = [defaultdict(int) for _ in range(k + 1)]
        dp[0][startPos] = 1
        
        for step in range(1, k + 1):
            for num in range(_min, _max + 1):
                dp[step][num] += dp[step - 1][num - 1] + dp[step - 1][num + 1]
                dp[step][num] %= mod
        

        return dp[k][endPos]