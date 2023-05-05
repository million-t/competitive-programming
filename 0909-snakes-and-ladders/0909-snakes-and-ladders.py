class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        
        boustr = {}
        cell = 1
        
        for row in range(N):
            for col in range(N):
                
                if not row%2:
                    boustr[cell] = (N - row - 1, col)
                
                else:
                    boustr[cell] = (N - row - 1, N - col - 1)
                
                cell += 1
        
        
        target = N*N
        queue = deque([1])
        visited = set([1])
        moves = 0
        
    
        while queue:
            
            size = len(queue)
            for _ in range(size):
                bous = queue.popleft()
                
                
                row, col = boustr[bous]
                if board[row][col] != -1:
                    bous = board[row][col]
                    
                if bous == target:
                    return moves
            
            
                for move in range(bous + 1, min(bous + 6, target) + 1):
                    
                    if move not in visited:
                        visited.add(move)            
                        queue.append(move)

            moves += 1
        
        return -1
                    
                