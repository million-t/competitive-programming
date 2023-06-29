class Solution:
    
    
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        source = (0, 0)
        key_count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = grid[row][col]
                if val == '@':
                    source = (row, col)
                
                elif val.isalpha() and val.islower():
                    key_count += 1
        
        
        discovered_keys = 0
        unlocked = 0
        queue = deque([(*source, discovered_keys, unlocked)])
        visited = set([(*source, discovered_keys, unlocked)])
        
        target = 0
        for ind in range(key_count):
            target |= 1 << ind
        
        path_len = 0
        while queue:
            
            size = len(queue)
            for _ in range(size):
                row, col, discovered, unlocked = queue.popleft()
                
                if discovered == target:
                    return path_len
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if inbound(nr, nc) and grid[nr][nc] != '#':
                        token = grid[nr][nc]
                        
                        temp_discovered = discovered
                        temp_unlocked = unlocked
                        if token.islower():
                            temp_discovered |= 1 << (ord(token) - ord('a'))
                        
                        elif token.isupper():
                            bit_map = ord(token) - ord('A')
                            if temp_discovered & 1 << bit_map:
                                temp_unlocked |= 1 << bit_map
                            
                            else:
                                continue
                        
                        if (nr, nc, temp_discovered, temp_unlocked) not in visited:
                            queue.append((nr, nc, temp_discovered, temp_unlocked))
                            visited.add((nr, nc, temp_discovered, temp_unlocked))
                        
            path_len += 1
        
        return -1
            
            
            
            
            
            
            
            
            
            
            
            
            
            