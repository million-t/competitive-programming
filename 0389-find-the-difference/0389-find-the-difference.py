class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        count = {}
        
        for lett in s:
            count[lett] = count.get(lett, 0) + 1
        
        for letter in t:
            count[letter] = count.get(letter, 0) - 1
        
            if count[letter] == -1:
                return letter
        