class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        s_vow = []
        
        for char in s:
            if char in vowels:
                s_vow.append(char)
        
        s_vow.sort()
        indx = 0
        ans = []
        for char in s:
            if char in vowels:
                ans.append(s_vow[indx])
                indx += 1
            
            else:
                ans.append(char)
        
        return ''.join(ans)
        