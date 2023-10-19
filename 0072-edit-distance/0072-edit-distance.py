class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(indx1, indx2):
            
            if indx2 < 0:
                return indx1 + 1
            
            elif indx1 < 0:
                return indx2 + 1
            
            if word1[indx1] == word2[indx2]:
                return dp(indx1 - 1, indx2 - 1)
            
            else:
                ans1 = dp(indx1, indx2 - 1) + 1
                ans2 = dp(indx1 - 1, indx2) + 1
                ans3 = dp(indx1 - 1, indx2 - 1) + 1
                return min(ans1, ans2, ans3)
            
            
        return dp(len(word1) - 1, len(word2) - 1)