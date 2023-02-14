class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr, s_size = 0, len(s) 

        for t_ptr in range(len(t)):
            
            if s_ptr < s_size and s[s_ptr] == t[t_ptr]:
                s_ptr += 1
        
        return s_ptr == s_size
    