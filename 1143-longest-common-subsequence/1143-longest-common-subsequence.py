class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        @cache
        def dp(indx1, indx2):
            if indx1 < 0 or indx2 < 0:
                return 0
            
            if text1[indx1] == text2[indx2]:
                return 1 + dp(indx1 - 1, indx2 - 1)
            
            return max(dp(indx1, indx2 - 1), dp(indx1 - 1, indx2))
        
        return dp(len(text1) - 1, len(text2) - 1)