class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def inbound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(row, col):
            if (not inbound(row, col)) or board[row][col] != 'O':
                return
            
            board[row][col] = '+'
            
            for r_change, c_change in directions:
                dfs(row + r_change, col + c_change)
                
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == '+':
                    board[row][col] = 'O'
                
                else:
                    board[row][col] = 'X'
            