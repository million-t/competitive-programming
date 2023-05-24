class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for ind in range(1, len(prices)):
            profit += max(0, prices[ind] - prices[ind - 1])
        
        return profit
        
        
        