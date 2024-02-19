class Solution:
    def minFlips(self, target: str) -> int:
        
        ans = 0
        cur = "0"
        
        for char in target:
            if char != cur:
                cur = char
                ans += 1
        
        return ans
        