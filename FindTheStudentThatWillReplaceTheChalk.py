class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = []
        curChalks = 0
        for c in chalk:
            curChalks += c
            prefix.append(curChalks)
        k = k % prefix[-1]
        for i, c in enumerate(chalk):
            if k < c:
                return i
            elif k == c:
                return i + 1
            k -= c
        
        

