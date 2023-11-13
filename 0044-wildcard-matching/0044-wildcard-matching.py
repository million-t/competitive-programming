class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dp(s_indx, p_indx):
            
            if s_indx == len(s) and p_indx == len(p):
                return True
            
            if s_indx < len(s) and p_indx == len(p):
                return False
            
            if s_indx == len(s) and p_indx < len(p):
                if p[p_indx] == '*':
                    return dp(s_indx, p_indx + 1)
                
                return False
            
            if p[p_indx] == s[s_indx] or p[p_indx] == '?':
                return dp(s_indx + 1, p_indx + 1)
            
            elif p[p_indx] == '*':
                return dp(s_indx + 1, p_indx + 1) or dp(s_indx + 1, p_indx) or dp(s_indx, p_indx + 1)
            
            return False
        
        return dp(0, 0)
                
        