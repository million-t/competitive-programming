class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        for indx in range(len(num) - 1, -1, -1):
            if int(num[indx]) & 1:
                return num[:indx + 1]
        
        return ""