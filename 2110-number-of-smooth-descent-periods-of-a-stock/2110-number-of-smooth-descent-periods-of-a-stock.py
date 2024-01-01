class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        
        ans = 1
        left = 0
        
        for right in range(1, len(prices)):
            if prices[right - 1] - 1 != prices[right]:
                left = right
            ans += right - left + 1
        
        return ans