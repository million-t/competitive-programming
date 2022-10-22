class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        l, r = 0, 0
        for r in range(len(chars)):
            if chars[l]!=chars[r]:
                s+=chars[l]
                if r-l!=1:
                    s+=str(r-l)
                l=r
        s+=chars[l]
        if r-l:
            s+=str(r-l+1)
        i = 0
        for c in s:
            chars[i] = c
            i+=1
        return len(s)

            


