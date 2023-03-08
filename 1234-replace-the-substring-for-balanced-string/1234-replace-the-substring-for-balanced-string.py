class Solution:
    def balancedString(self, s: str) -> int:
        length = len(s)
        letter_count = Counter(s)
        
        target = Counter()
        
        for let, count in letter_count.items():
            if count > length//4:
                target[let] = count - length//4
                
        if not target:
            return 0
        
        
        window = Counter()
        left = 0
        
        min_len = float("inf")
        for right in range(length):
            window[s[right]] += 1
            
            while left <= right and target <= window:
                min_len = min(min_len, right - left + 1)
                window[s[left]] -= 1
                left += 1
            
        return min_len
        