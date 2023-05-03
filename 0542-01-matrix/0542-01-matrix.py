class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        
        def inbounds(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        ans = [[0]*len(mat[0]) for _ in range(len(mat))]
        
        visited = set()
        queue = deque()
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                
                if not mat[row][col]:
                    queue.append((row, col))
                    visited.add((row, col))
        
        distance = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                row, col = queue.popleft()
                
                if mat[row][col]:
                    ans[row][col] = distance
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    
                    if inbounds(nr, nc) and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            distance += 1
        
        return ans