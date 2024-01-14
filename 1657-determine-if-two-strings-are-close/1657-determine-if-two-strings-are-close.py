class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        vals1 = sorted(c1.values())
        vals2 = sorted(c2.values())
        if sorted(c1.keys()) != sorted(c2.keys()):
            return False
        
        return vals1 == vals2