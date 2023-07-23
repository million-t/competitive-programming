class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        
        if length < 2:
            return 0
        
        sold_dp = [0]*(length + 1)
        bought_dp = [float('-inf')]*(length + 1)
        bought_dp[0] = -prices[0]
        
        for ind, price in enumerate(prices):
            bought_dp[ind] = max(bought_dp[ind], bought_dp[ind - 1], sold_dp[ind - 2] - price)
            sold_dp[ind] = max(sold_dp[ind], sold_dp[ind - 1], bought_dp[ind - 1] + price)
            
        
        return max(bought_dp[-2], sold_dp[-2])