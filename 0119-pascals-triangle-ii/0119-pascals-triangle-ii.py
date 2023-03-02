class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        elif rowIndex == 1:
            return [1, 1]
        
        newRow = [1]*(rowIndex + 1)
        intermediate = self.getRow(rowIndex - 1) 
        
        for i in range(1, rowIndex):
            newRow[i] = intermediate[i-1] + intermediate[i]
        
        return newRow