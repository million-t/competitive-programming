class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        size = len(prices)
        held = [0]*size
        not_held = [0]*size
        held[0] = -prices[0]
        
        
        for ind in range(1, size):
            price = prices[ind]
             
            sell = price + held[ind - 1] - fee 
            not_held[ind] = max(not_held[ind - 1], sell)
            
            buy = not_held[ind - 1] - price
            held[ind] = max(held[ind - 1], buy) 
            
        
        
        return not_held[-1]
        