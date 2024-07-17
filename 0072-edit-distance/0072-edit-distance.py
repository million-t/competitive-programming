class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(index1, index2):
            if index2 < 0:
                return index1 + 1
            elif index1 < 0:
                return index2 + 1
            
            # characters already match
            if word1[index1] == word2[index2]:
                return dp(index1 - 1, index2 - 1)
            
            else:
                # insert a character
                ans1 = dp(index1, index2 - 1) + 1
                # delete a character
                ans2 = dp(index1 - 1, index2) + 1
                # replace a character
                ans3 = dp(index1 - 1, index2 - 1) + 1
                return min(ans1, ans2, ans3)
            
        return dp(len(word1) - 1, len(word2) - 1)
