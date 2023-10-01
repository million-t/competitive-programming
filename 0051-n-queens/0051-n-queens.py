class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        for_diag = set()
        back_diag = set()
        vert = set()
        horiz = set()
        ans = []
        board = [["."]*n for row in range(n)]
        
        def backtrack(row, for_diag, back_diag, vert, horiz):
            
            if row >= n:
                ansi = []
                for line in board:
                    ansi.append(''.join(line))
                    
                ans.append(ansi)
                return
                
            for col in range(n):
                if col not in vert and row + col not in for_diag and row - col not in back_diag:
                    vert.add(col)
                    for_diag.add(row + col)
                    back_diag.add(row - col)
                    board[row][col] = 'Q'
                    backtrack(row + 1, for_diag, back_diag, vert, horiz)
                    board[row][col] = '.'
                    vert.remove(col)
                    for_diag.remove(row + col)
                    back_diag.remove(row - col)
        
        backtrack(0, for_diag, back_diag, vert, horiz)
        return ans