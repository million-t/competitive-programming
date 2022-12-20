class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)<2: return True
        pos = {c:i for i,c in enumerate(order)}
        def rightOrder(a,b):
            for i in range(min(len(a), len(b))):
                if pos[a[i]] < pos[b[i]]:
                    return True
                elif pos[a[i]] > pos[b[i]]:
                    return False
            return True if len(a) <= len(b) else False
        
        for i in range(1, len(words)):
            if not rightOrder(words[i-1], words[i]):
                return False
        return True
                
                
        
