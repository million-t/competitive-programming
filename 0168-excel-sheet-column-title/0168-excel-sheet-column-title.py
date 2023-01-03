class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans_reversed = []
        ordOf_A = 65
        
        while columnNumber:
            #columnNumber should be reduced by one to get the right remainder 
            remainder = (columnNumber - 1)%26
            columnNumber = (columnNumber - 1)//26
            ans_reversed.append(chr(ordOf_A + remainder))
        
        ans = ans_reversed[::-1]
        ans_as_str = ''.join(ans)
        return ans_as_str
        