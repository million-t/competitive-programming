class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 2}
        
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        prev1 = self.climbStairs(n - 2)
        prev2 = self.climbStairs(n - 1)
        
        self.memo[n] = prev1 + prev2
        return prev1 + prev2

