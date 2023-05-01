class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        
        directions = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]
        
        def isExit(row, col):
            return row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[-1]) - 1
        
        def inbound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        
        
        visited = set([entrance])
        queue = deque([entrance])
        steps = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                row, col = queue.popleft()
                
                if (row, col) != entrance and isExit(row, col):
                    return steps
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    if inbound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == '.':
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            steps += 1
            
        return -1
                        