class DSU:
    def __init__(self, positions, col):
        
        self.rep = {pos: pos for pos in positions}
        self.rank = {pos: 1 for pos in positions}
        self.span = {pos: set([pos[1]]) for pos in positions}
        self.col = col
        
    
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
            return False
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
            self.span[rep_x].update(self.span[rep_y])
            
            if len(self.span[rep_x]) == self.col:
                return True
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
            self.span[rep_y].update(self.span[rep_x])
            
            if len(self.span[rep_y]) == self.col:
                return True
            
        else:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
            self.span[rep_x].update(self.span[rep_y])
            if len(self.span[rep_x]) == self.col:
                return True
        
        return False
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        def inbound(r, c):
            return 1<= r <= row and 1 <= c <= col
        
        for ind in range(len(cells)):
            cells[ind] = tuple(cells[ind])
        
        
        union_find = DSU(cells, col)
        seen = set()
        ind = 0
        
        for x, y in cells:
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy 
                if inbound(nx, ny) and (nx, ny) in seen:
                    if union_find.union((x, y), (nx, ny)):
                        return ind
            
            seen.add((x, y))
            ind += 1
            
        return ind 