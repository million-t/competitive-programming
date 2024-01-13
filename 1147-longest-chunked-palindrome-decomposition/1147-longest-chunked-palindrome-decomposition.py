class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        
        rev = text[::-1]
        count = 0
        start = 0
        
        for i_rev in range(len(text)//2):            
            yes = True
            
            for indx in range(start, i_rev + 1):
                if text[indx] != rev[i_rev - indx + start]:
                    yes = False
                    break                
            
            if yes:
                count += 1
                start = i_rev + 1

        return 2*count + (start < (len(text) + 1)//2)