class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lastRow = [1]
        
        for i in range(1, rowIndex + 1):
            newRow = [1]
            
            for j in range(1, i):
                newRow.append(lastRow[j - 1] + lastRow[j])
                
            newRow.append(1)
            lastRow = newRow
        
        return lastRow