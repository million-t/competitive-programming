class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        size = len(questions)
        dp = [0]*size
        dp[-1] = questions[-1][0]
        
        for ind in range(size - 2, -1, -1):
            points, brainpower = questions[ind]
            
            if brainpower + ind + 1 >= size:
                dp[ind] = max(points, dp[ind + 1])
            
            else:
                dp[ind] = max(points + dp[ind + brainpower + 1], dp[ind + 1])
        
        
        return dp[0]
                
        