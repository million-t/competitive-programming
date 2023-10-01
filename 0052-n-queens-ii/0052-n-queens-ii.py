class Solution:
    def totalNQueens(self, n: int) -> int:
        
        for_diag = set()
        back_diag = set()
        vert = set()
        horiz = set()
        ans = 0
        
        
        def backtrack(row, for_diag, back_diag, vert, horiz):
            nonlocal ans
            
            if row >= n:
                ans += 1
                
            for col in range(n):
                if col not in vert and row + col not in for_diag and row - col not in back_diag:
                    vert.add(col)
                    for_diag.add(row + col)
                    back_diag.add(row - col)
                    backtrack(row + 1, for_diag, back_diag, vert, horiz)
                    vert.remove(col)
                    for_diag.remove(row + col)
                    back_diag.remove(row - col)
        
        backtrack(0, for_diag, back_diag, vert, horiz)
        return ans