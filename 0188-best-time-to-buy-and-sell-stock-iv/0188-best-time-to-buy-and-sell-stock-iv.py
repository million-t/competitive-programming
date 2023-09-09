class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        memo = {}
        def dp(ind, k, state):
            
            key = (ind, k, state)
            if key in memo:
                return memo[key]
            
            if not k or ind >= len(prices):
                return 0
            
            cur_max = 0
            if state == 'bought':
                sell_now = dp(ind + 1, k - 1, 'sold') + prices[ind]
                skip = dp(ind + 1, k, 'bought')
                cur_max = max(sell_now, skip)
            
            else:
                buy_now = dp(ind + 1, k, 'bought') - prices[ind]
                skip = dp(ind + 1, k, 'sold')
                cur_max = max(buy_now, skip)
            
            memo[key] = cur_max
            return cur_max
        
        return dp(0, k, 'sold')
    