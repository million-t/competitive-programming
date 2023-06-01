class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        
        dp = [float("inf")]*(amount + 1)
        dp[0] = 1
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for num in range(1, amount + 1):
            
            for coin in coins:
                
                if num >= coin:
                    dp[num] = min(dp[num], dp[num - coin] + 1) 
        
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]