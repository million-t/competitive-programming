class DSU:
    def __init__(self, n):
        
        self.rep = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        
        root = x
        while root != self.rep[root]:
            root = self.rep[root]
        
        while x != root:
            temp = self.rep[x]
            self.rep[x] = root
            x = temp
        
        return root
    
    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        
        if rep_x == rep_y:
            return
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
        
        else:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        ROWS, COLS = len(grid), len(grid[0])
        union_find = DSU(ROWS*COLS)
        
        moves = {
            1: ((0, -1), (0, 1)),
            2: ((-1, 0), (1, 0)),
            3: ((0, -1), (1, 0)),
            4: ((0, 1), (1, 0)),
            5: ((0, -1), (-1, 0)),
            6: ((0, 1), (-1, 0))
        }
        
        def inbound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        seen = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                index = row*COLS + col
                
                move = grid[row][col]
                for dr, dc in moves[move]:
                    nr = row + dr
                    nc = col + dc
                    
                    if not inbound(nr, nc):
                        continue
                    
                    neigh_ind = nr*COLS + nc
                    connection = tuple(sorted([index, neigh_ind]))
                    
                    if connection in seen:
                        union_find.union(index, neigh_ind)
                        seen.remove(connection)                        
                    else:
                        seen.add(connection)
        
        
        last_ind = (ROWS - 1)*COLS + (COLS - 1)
        return union_find.is_connected(0, last_ind)
                        
                    
                    
                
                
        
        
        
        