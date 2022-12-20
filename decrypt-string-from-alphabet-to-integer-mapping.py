class Solution:
    def freqAlphabets(self, s: str) -> str:    
        ans = ''
        if len(s)<3:
            ans+= chr(ord('a')+int(s)-1)
        l, r = 0, 2
        while l<len(s):
            if s[l] == '#':
                l+=1
                r+=1
                continue
            if r<len(s) and s[r] == '#':
                ans += chr(ord('a')+int(s[l:r])-1)
                l+=3
                r+=3
            else:
                ans+= chr(ord('a')+int(s[l])-1)
                l+=1
                r+=1
        return ans
