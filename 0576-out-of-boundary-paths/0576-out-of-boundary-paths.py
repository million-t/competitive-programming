class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if not maxMove:
            return 0
        
        dp = [[0]*n for _ in range(m)]
        for row in range(m):
            dp[row][0] += 1
            dp[row][-1] += 1
        
        for col in range(n):
            dp[0][col] += 1
            dp[-1][col] += 1
        
        movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def inbounds(r, c): return 0 <= r < m and 0 <= c < n
        mod = 10**9 + 7
        
        ans = dp[startRow][startColumn]
        for moves in range(1, maxMove):
            new_dp = [[0]*n for _ in range(m)]
            
            for row in range(m):
                for col in range(n):   
                    for dr, dc in movement:
                        nr, nc = row + dr, col + dc
                        if inbounds(nr, nc):
                            new_dp[row][col] += dp[nr][nc]               
                            new_dp[row][col] %= mod
            dp = new_dp
            ans += dp[startRow][startColumn]
            ans %= mod
            
        return ans         