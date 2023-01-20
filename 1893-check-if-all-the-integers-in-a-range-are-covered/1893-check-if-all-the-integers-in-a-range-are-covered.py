class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = [0]*52
        
        for start, end in ranges:
            cover[start] += 1
            cover[end + 1] -= 1
        
        prefix = 0
        for i in range(51):
            cover[i] += prefix
            prefix = cover[i]
        
        for i in range(left, right + 1):
            if not cover[i]:
                return False
        
        return True