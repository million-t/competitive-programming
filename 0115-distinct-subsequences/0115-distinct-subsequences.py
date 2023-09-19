class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        length = len(s)
        dp = { ind: 1 for ind in range(length) }
        start = 0
        
        for char in t:
            
            new_dp = defaultdict(int)
            new_start = length
            
            for ind in range(start, length):
                letter = s[ind]
                if char == letter:
                    new_dp[ind + 1] = new_dp[ind] + dp[ind]
                    new_start = min(new_start, ind)
                
                else:
                    new_dp[ind + 1] = new_dp[ind]
            
            dp = new_dp
            start = new_start + 1
                    
        return dp[length]
                
        