class Solution:
    def countVowels(self, word: str) -> int:
        
        length = len(word)
        right = length
        ans = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        for indx, char in enumerate(word):
            left = indx + 1
            if char in vowels:
                ans += left*right
            
            right -= 1
        
        return ans
        