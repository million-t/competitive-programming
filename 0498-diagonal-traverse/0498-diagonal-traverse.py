class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        diag = defaultdict(list)
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                diag[row + col].append(mat[row][col])
        
        
        ans = []
        for key in sorted(diag.keys()):
            ans.extend(diag[key] if key%2 else diag[key][::-1])
        
        return ans