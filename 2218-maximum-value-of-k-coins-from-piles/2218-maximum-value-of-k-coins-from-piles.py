class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        
        dp = [0]*(k + 1)
        new_dp = []
        
        for pile in piles:
            pref = 0
            new_dp = [0]*(k + 1)
            for indx, coins in enumerate(pile):
                pref += coins
                for num in range(k, indx, - 1):
                    new_dp[num] = max(new_dp[num], dp[num], dp[num - indx - 1] + pref)
            
            dp = new_dp
            
        return dp[k]
        
        