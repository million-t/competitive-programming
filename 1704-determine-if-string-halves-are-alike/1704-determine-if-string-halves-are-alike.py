class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("AaEeIiOoUu")
        length = len(s)
        
        def count(txt):
            
            num = 0
            for char in txt:
                if char in vowels:
                    num += 1
            
            return num
        
        return count(s[:length//2]) == count(s[length//2:])
        
        