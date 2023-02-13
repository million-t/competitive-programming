class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        max_length = 0
        odd_counted = 0
        
        for c in count.values():
            max_length += 2*(c//2)
            
            if not odd_counted and c%2:
                odd_counted += 1
        
        return max_length + odd_counted
        