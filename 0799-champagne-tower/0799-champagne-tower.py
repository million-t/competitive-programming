class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        dp = [poured]
        
        for row in range(1, query_row + 1):
            temp = [0]*(row + 1)
            
            for glass in range(row + 1):
                if not glass:
                    temp[glass] = max((dp[glass] - 1)/2, 0)
                
                elif glass == row:
                    temp[glass] = max((dp[glass - 1] - 1)/2, 0)
                
                else:
                    temp[glass] = max(0, (dp[glass - 1] - 1)/2) + max((dp[glass] - 1)/2, 0)
            
            dp = temp
        
        return min(1, dp[query_glass])
                    