class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonals = defaultdict(set)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diagonals[row - col].add(matrix[row][col])
        
        for curSet in diagonals.values():
            if len(curSet) > 1:
                return False
        return True
        