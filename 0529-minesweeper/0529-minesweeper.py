class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (-1, 1),
            (1, -1),
            (-1, -1),
            (1, 1)
        ]
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def mineAround(row, col):
            
            mines = 0
            for dr, dc in directions:
                nRow, nCol = row + dr, col + dc
                    
                if inbound(nRow, nCol) and board[nRow][nCol] in 'MX':
                    mines += 1
            
            return mines
                
        
        

        def dfs(row, col):
            
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return 
            
            elif board[row][col] == "E":
                
                mines_around = mineAround(row, col)
                if mines_around:
                    board[row][col] = str(mines_around)
                    return
                
                board[row][col] = 'B'
                for dr, dc in directions:
                    nRow, nCol = row + dr, col + dc
                    
                    if inbound(nRow, nCol) and board[nRow][nCol] in 'E':
                        dfs(nRow, nCol)
                        
                
                    
            return 0
        
        dfs(click[0], click[1])
        return board 
                    
            
            
        
        