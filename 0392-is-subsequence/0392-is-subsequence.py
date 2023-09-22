class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        
        
        ptr_t = 0
        
        for ptr_s, char in enumerate(s):
            while ptr_t < len(t) and t[ptr_t] != char:
                ptr_t += 1
            
            if ptr_t >= len(t):
                return False
            
            else:
                ptr_t += 1
        
        return True
        
        
        