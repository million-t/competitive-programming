class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        ans = 0
        avail = Counter(chars)
        
        for word in words:
            count = Counter(word)
            if count <= avail:
                ans += len(word)
        
        return ans
        