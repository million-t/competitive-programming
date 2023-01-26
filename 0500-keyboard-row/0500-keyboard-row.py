class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        
        ans = []
        for word in words:
            letters = set(word.lower())
            if letters.issubset(row1) or letters.issubset(row2) or letters.issubset(row3):
                ans.append(word)
                
        return ans