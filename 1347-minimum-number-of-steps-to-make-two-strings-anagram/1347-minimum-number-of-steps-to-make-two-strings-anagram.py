class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s = Counter(s)
        t = Counter(t)
        
        ans = 0
        for _ord in range(ord('a'), ord('z') + 1):
            char = chr(_ord)
            ans += max(s[char] - t[char], 0)
        
        return ans