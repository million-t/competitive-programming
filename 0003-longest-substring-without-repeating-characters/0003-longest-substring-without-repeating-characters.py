class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        
        max_len = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while count[s[right]] > 1:
                count[s[left]] = count.get(s[left], 0) - 1
                
                if not count[s[left]]:
                    count.pop(s[left])
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
        
        