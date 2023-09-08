class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0
        
        min_before = float('inf')
        dp = []
        
        for num in prices:
            dp.append(max(num - min_before, 0))
            min_before = min(min_before, num)
            
        
        
        max_suf = [0]*length

        for ind in range(length - 2, -1, -1):
            max_suf[ind] = max(max_suf[ind + 1], prices[ind + 1])
        
        ans = max(dp)
        max_first_transaction_before = dp[1]

        for ind in range(2, length - 1):
            ans = max(ans, max_first_transaction_before + max_suf[ind] - prices[ind])
            max_first_transaction_before = max(max_first_transaction_before, dp[ind])
        
        return ans