class Solution:
    def arrangeWords(self, text: str) -> str:
        
        words = text.split()
        words[0] = words[0].lower()
        words.sort(key= lambda x: len(x))
        words[0] = words[0][0].upper() + words[0][1:]
        
        return " ".join(words)