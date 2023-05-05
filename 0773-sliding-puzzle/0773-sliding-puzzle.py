class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbounds(row, col): return 0 <= row < 2 and 0 <= col < 3
        
        visited = set()
        queue = deque()
        
        
        for row in range(2):
            for col in range(3):
                
                if not board[row][col]:
                    start_state = tuple([ tuple(row) for row in board ])
                    queue.append((row, col, start_state))
                    visited.add(start_state)
                    break
                    
        
        target = ((1, 2, 3), (4, 5, 0))
        moves = 0
        
        while queue:
            
            size = len(queue)
            for _ in range(size):
                row, col, state = queue.popleft()
                
                if state == target:
                    return moves
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    
                    if inbounds(nr, nc):
                        _next = [ list(row) for row in state ]
                        _next[row][col], _next[nr][nc] = _next[nr][nc], _next[row][col]
                        _next = tuple([ tuple(row) for row in _next ])
                
                        if _next not in visited:
                            visited.add(_next)
                            queue.append((nr, nc, _next))
                        
                        
            
            moves += 1
        
        return -1
                    
        