class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t = Counter(t)
        win_count = Counter()
        
        left = 0
        min_len = left, float('inf')
        
        for right in range(len(s)):
            win_count[s[right]] += 1
            
            while win_count >= count_t:
                
                if min_len[1] - min_len[0] > right - left:
                    min_len = left, right
                    
                win_count[s[left]] -= 1
                left += 1
        
        
        if min_len[1] == float('inf'):
            return ''
        
        return s[min_len[0]: min_len[1] + 1]
                
        