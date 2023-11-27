class Solution:
    def minimumSteps(self, s: str) -> int:
        
        ans = 0
        indx = 0
        for i, let in enumerate(s):
            if let == '0':
                ans += i - indx
                indx += 1
            
        
        return ans