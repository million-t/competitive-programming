class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(map(lambda x: ord(x) - 97, s))
        
        prefix_s = [0]*len(s)
        
        for start, end, direction in shifts:
            prefix_s[start] += 1 if direction else -1
            
            if end + 1 < len(s):
                prefix_s[end + 1] += -1 if direction else 1
        
        for i in range(1, len(prefix_s)):
            prefix_s[i] += prefix_s[i-1]
            
        
        for i in range(len(s)):
            s[i] = chr((s[i] + prefix_s[i])%26 + 97) 
        
        # s = list(map(lambda x: chr(x  + 97), s))
        
        return ''.join(s)