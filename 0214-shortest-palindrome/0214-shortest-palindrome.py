class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        
        left, right = 0, 1
        length = len(s)
        lps = [0]*length
        
        while right < length:
            if s[right] == s[left]:
                lps[right] = left + 1
                left += 1
                right += 1
            
            elif not left:
                right += 1
            
            else:
                left = lps[left - 1]
        

        left, right = 0, length - 1
        
        while left < right:
            if s[right] == s[left]:
                left += 1
                right -= 1
            
            elif not left:
                right -= 1
            
            else:
                left = lps[left - 1]
            

            if left == right:
                return s[:left + right:-1] + s
            
            elif left > right:
                return s[:left + left - 1:-1] + s
            
            
        return s