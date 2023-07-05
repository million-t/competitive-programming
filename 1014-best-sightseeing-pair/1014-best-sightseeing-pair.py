class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        
        dp = [0]
        for ind, val in enumerate(values):
            dp.append(max(dp[-1], val + ind))
            
        max_score = 0 
        for ind in range(len(values) - 1, 0, -1):
            val = values[ind]    
            max_score = max(max_score, dp[ind] + val - ind)
        
        return max_score