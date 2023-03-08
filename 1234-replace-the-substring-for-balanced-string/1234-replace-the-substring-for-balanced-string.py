class Solution:
    def balancedString(self, s: str) -> int:
        length = len(s)
        letter_count = Counter(s)
        
        to_be_replaced = ''
        
        for let, count in letter_count.items():
            if count > length//4:
                to_be_replaced += let*(count - length//4 )
        
        if not to_be_replaced:
            return 0
        
        target = Counter(to_be_replaced)
        
        
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
        