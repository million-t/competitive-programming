class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        win_size = len(needle)
        size = len(haystack)
        
        for i in range(size):
            
            if i > size - win_size:
                break
            
            no = False
            for j in range(win_size):
                if haystack[i + j] != needle[j]:
                    no = True
                    break
            
            if not no:
                return i
        
        return -1
        