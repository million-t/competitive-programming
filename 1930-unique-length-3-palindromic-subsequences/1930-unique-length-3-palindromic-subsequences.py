class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        seen = defaultdict(int)
        red = defaultdict(int)
        ans = 0
        
        for char in s:
            indx = 1 << (ord(char) - ord('a'))
            
            if char in seen:
                inc = seen[char].bit_count()
                ans += inc - red[char]
                red[char] = inc
            
            
            for let in seen:
                seen[let] |= indx
            
            seen[char]
        

        return ans
                
            
        
        