class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(left, right, s):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left, right
        
        max_left = max_right = 0
        length = len(s)

        for ind in range(length):
            left, right = helper(ind, ind, s)
            
            if right - left > max_right - max_left:
                max_left, max_right = left, right
        
        
        for ind in range(1, length):
            left, right = helper(ind - 1, ind, s)
            
            if right - left > max_right - max_left:
                max_left, max_right = left, right
            
            
        
        return s[max_left + 1: max_right]
                
            
        