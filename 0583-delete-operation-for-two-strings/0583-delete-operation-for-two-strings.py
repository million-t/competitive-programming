class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        
        @cache
        def dp(indx1, indx2):
            if indx1 < 0 or indx2 < 0:
                return 0
            
            if word1[indx1] == word2[indx2]:
                return 1 + dp(indx1 - 1, indx2 - 1)
            
            return max(dp(indx1, indx2 - 1), dp(indx1 - 1, indx2))
        
        return len(word1) + len(word2) - 2*dp(len(word1) - 1, len(word2) - 1)