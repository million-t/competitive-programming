class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        memo = {}
        
        def dp(start, end):
            
            if start > end:
                return 0
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            ans = 0
            if s[start] == s[end]:
                ans = 2 + dp(start + 1, end - 1) - int(start == end) 
            
            else:
                ans = max(dp(start + 1, end), dp(start, end - 1))
            
            memo[(start, end)] = ans
            return ans
        
        
        return dp(0, len(s) - 1)