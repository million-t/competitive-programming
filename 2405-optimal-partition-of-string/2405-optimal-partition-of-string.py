class Solution:
    def partitionString(self, s: str) -> int:
        
        count = defaultdict(int)
        left = 0
        ans = 1
        
        for right, char in enumerate(s):
            
            if count[char] + 1 > 1:
                while left < right:
                    count[s[left]] -= 1
                    left += 1
                
                ans += 1
                
            count[char] += 1
        
        
                    
        return ans