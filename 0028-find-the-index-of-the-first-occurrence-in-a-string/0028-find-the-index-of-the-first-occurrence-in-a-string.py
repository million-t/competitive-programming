class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        
        needle_length = len(needle)
        lps = [0]*needle_length
        
        left, right = 0, 1
        
        while right < needle_length:
            
            if needle[left] == needle[right]:
                lps[right] = left + 1
                left += 1
                right += 1
            
            else:
                if not left:
                    right += 1
                
                else:
                    left = lps[left - 1]
        
        
        needle_indx = 0
        haystack_indx = 0
        
        while haystack_indx < len(haystack):
            if haystack[haystack_indx] == needle[needle_indx]:
                needle_indx += 1
                haystack_indx += 1
            
            elif not needle_indx:
                haystack_indx += 1
            
            else:
                needle_indx = lps[needle_indx - 1]
                
            if needle_indx == needle_length:
                return haystack_indx - needle_length
                
        
        return -1
        
                
            
            
            