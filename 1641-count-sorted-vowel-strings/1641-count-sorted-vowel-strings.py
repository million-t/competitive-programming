class Solution:
    def countVowelStrings(self, n: int) -> int:
        # vowels in order represented in dp => u, o, i, e, a 
        dp = [1]*5
        
        for size in range(1, n):
            for vowel_ind in range(1, 5):
                dp[vowel_ind] += dp[vowel_ind - 1]  
        
        return sum(dp)