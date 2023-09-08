class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(left, right, s):
            
            palindromes = 0
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                palindromes += 1
                
            return palindromes
        
        max_left = max_right = 0
        length = len(s)
        ans = 0
        
        for ind in range(length):
            ans += helper(ind, ind, s)        
        
        for ind in range(1, length):
            ans += helper(ind - 1, ind, s)
            
        
        return ans