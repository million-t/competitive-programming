class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dictionary_set = set(dictionary)
        memo = {}
        
        def dp(ind):
            if ind >= len(s):
                return 0
            
            if ind in memo:
                return memo[ind]
            
            
            temp = 1 + dp(ind + 1)
            
            for right in range(ind, len(s)):
                if s[ind: right + 1] in dictionary_set:
                    temp = min(temp, dp(right + 1))
            
            memo[ind] = temp
            return memo[ind]
        
        return dp(0)
        
        