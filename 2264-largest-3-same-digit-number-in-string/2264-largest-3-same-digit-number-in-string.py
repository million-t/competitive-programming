class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        prev = ""
        for indx in range(2, len(num)):
            segment = num[indx - 2: indx + 1]
            if len(set(segment)) == 1 and segment > prev:
                prev = segment
        
        return prev
        