class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [''.join(set(sorted(w))) for w in words]     
        count = {}
        for sett in words:
            count[sett] = count.get(sett, 0) + 1
        numPairs = 0
        for val in count.values():
            if val>=2:
                numPairs+= factorial(val)//(factorial(2)*factorial(val-2))
        return numPairs
        
