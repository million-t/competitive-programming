class DSU:
    def __init__(self, obj):
        self.rep = {num: num for num in obj}
        self.rank = {num: 1 for num in obj}
        self.size = {num: 1 for num in obj}
    
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
            self.size[rep_x] += self.size[rep_y]
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
            self.size[rep_y] += self.size[rep_x]
            
        else:
            self.rep[rep_y] = rep_x
            self.size[rep_x] += self.size[rep_y]
            self.rank[rep_x] += 1
    
    def getSize(self, x):
        return self.size[self.find(x)]
    
    def getMaxSize(self):
        
        if self.size:
            return max(self.size.values())
        
        return 1
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        comps = set()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    comps.add((row, col))
        
        union_find = DSU(comps)
        
        def inbounds(r, c): return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        directions = [(-1, 0), (0, -1)]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if inbounds(nr, nc) and grid[nr][nc]:
                            union_find.union((row, col), (nr, nc))
        
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = union_find.getMaxSize()
        
        
        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    
                    temp = {}
                    for indx in range(4):
                        dr, dc = neighbours[indx]
                        fr, fc = row + dr, col + dc
                        
                        if not inbounds(fr, fc) or not grid[fr][fc]:
                            continue
                        
                        rep = union_find.find((fr, fc))
                        temp[rep] = union_find.getSize((fr, fc))
                    
                    ans = max(ans, sum(temp.values()) + 1)
                        
        
        return ans
                    
                
                
                
                
                            
                            
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        
        
        