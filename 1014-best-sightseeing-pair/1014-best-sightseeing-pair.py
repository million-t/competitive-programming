class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        
        prev_dp = 0
        max_score = 0 
        
        for ind, val in enumerate(values):
            max_score = max(max_score, prev_dp + val - ind)
            prev_dp = max(prev_dp, val + ind)
            
        return max_score