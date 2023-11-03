class DSU:
    def __init__(self, objs):
        
        self.rep = {obj: obj for obj in objs}
        self.rank = {obj: 1 for obj in objs}
    
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
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        components = [(row, col) for col in range(cols) for row in range(rows) if grid[row][col] == "1"]
        union_find = DSU(components)
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue
                
                if row > 0 and grid[row - 1][col] == "1":
                    union_find.union((row, col), (row - 1, col))
                
                if col > 0 and grid[row][col - 1] == "1":
                    union_find.union((row, col), (row, col - 1))
        
        return len(set([union_find.find((row, col)) for col in range(cols) for row in range(rows) if grid[row][col] == "1"]))
        
                    
        
        
        
        
        
        
        