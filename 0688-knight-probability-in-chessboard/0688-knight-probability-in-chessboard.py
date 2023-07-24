class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        def inbound(r, c, n):
            return 0 <= r < n and 0 <= c < n
        
        
        board = [[[1, 1] for col in range(n)] for r in range(n)]
        directions = [(1, 2), (1, -2), 
                      (2, 1), (2, -1),
                      (-1, 2), (-1, -2),
                      (-2, 1), (-2, -1)]
        
        
        for moves in range(k):
            for r in range(n):
                for c in range(n):
                    
                    board[r][c][0] = board[r][c][1]
                    probs = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        if inbound(nr, nc, n):
                            if nr < r:
                                probs += board[nr][nc][0]
                            else:
                                probs += board[nr][nc][1]
                                
                    board[r][c][1] = probs/8
        
        
        return board[row][column][1]
        
        
                
        