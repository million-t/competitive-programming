class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev2 = 0
        prev1 = 1
        
        for steps in range(2, n + 2):
            temp = prev1
            prev1 = prev1 + prev2
            prev2 = temp
        
        return prev1
            
        
        