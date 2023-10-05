class Solution:
    def knightDialer(self, n: int) -> int:
        
        mod = 10**9 + 7
        
        dp = [defaultdict(int) for _ in range(n)]
        temp = {
            0: (6, 4),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }
        
        for dig in temp:
            dp[0][dig] = 1
        
        for jump in range(1, n):
            for digit in temp:
                for valid_prev in temp[digit]:
                    dp[jump][digit] = (dp[jump][digit] + dp[jump - 1][valid_prev])%mod
        
    
        return sum(dp[n - 1].values())%mod
        
        