class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        dp = defaultdict(int)
        dp[0] = 1
        
        for coin in coins:
            
            for ind in range(coin, amount + 1):
                dp[ind] += dp[ind - coin]
            
        
        return dp[amount]
                
        