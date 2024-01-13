class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        
        ans = 0
        s = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            lval = s[left]
            rval = s[right]
            
            if lval == rval:
                left += 1
                right -= 1
                continue
            
            next_lval = right - 1
            next_rval = left + 1
            
            while next_lval >= 0 and s[next_lval] != lval:
                next_lval -= 1
            
            while next_rval < len(s) and s[next_rval] != rval:
                next_rval += 1
            
            if next_lval < 0 or next_rval - left <= right - next_lval:
                for _ in range(next_rval - left):
                    s[next_rval - 1], s[next_rval] = s[next_rval], s[next_rval - 1]
                    next_rval -= 1
                    ans += 1
            else:
                for _ in range(right - next_lval):
                    s[next_lval + 1], s[next_lval] = s[next_lval], s[next_lval + 1]
                    next_lval += 1
                    ans += 1
            
            
            left += 1
            right -= 1
        

        return ans
                
        