class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        length = len(s)
        pref = [0]*(length + 1)
        
        for start, end, _dir in shifts:
            inc = 1 if _dir else -1
            
            pref[start] += inc
            pref[end + 1] -= inc
        
        for ind in range(1, length + 1):
            pref[ind] += pref[ind - 1]
        
        ans = []
        ord_a = ord('a')

        for ind, char in enumerate(s):

            ans.append(chr(ord_a + ((ord(char) - ord_a + pref[ind])%26)))
        

        return ''.join(ans)
            
            
        
        
        