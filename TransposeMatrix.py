
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMat= []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            newMat.append(row)
        return newMat



        
