class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        temp = [(age, score) for age, score in zip(ages, scores)]
        temp.sort()
        length = len(scores)
        
        dp = defaultdict(int)
        max_score = 0
        
        for ind in range(length):
            age, score = temp[ind]
            dp[ind] = score
            
            for sec_ind in range(ind):
                prev_age, prev_score = temp[sec_ind]
                
                if prev_age == age or prev_score <= score:
                    dp[ind] = max(dp[ind], dp[sec_ind] + score)
                    
            max_score = max(max_score, dp[ind])
        
        return max_score
        
        