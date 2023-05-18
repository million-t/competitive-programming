class DSU:
    def __init__(self, n):
        
        self.rep = {num: num for num in range(1, n + 1)}
        self.rank = [0]*(n + 1)
        self.minRoad = [float('inf')]*(n + 1)
    
    def find(self, x):
        
        root = x
        while root != self.rep[root]:
            root = self.rep[root]
        
        while x != root:
            temp = self.rep[x]
            self.rep[x] = root
            x = temp
        
        return root
    
    def union(self, x, y, dist):
        rep_x = self.find(x)
        rep_y = self.find(y)
        
        if rep_x == rep_y:
            self.minRoad[rep_x] = min(self.minRoad[rep_x], dist)
            return
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.minRoad[rep_x] = min(self.minRoad[rep_x], self.minRoad[rep_y], dist)
            self.rep[rep_y] = rep_x
            
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.minRoad[rep_y] = min(self.minRoad[rep_y], self.minRoad[rep_x], dist)
            self.rep[rep_x] = rep_y
        
        else:
            self.minRoad[rep_x] = min(self.minRoad[rep_x], self.minRoad[rep_y], dist)
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getMinRoad(self, rep):
        return self.minRoad[rep]
    

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        union_find = DSU(n)
        
        for a, b, dist in roads:
            union_find.union(a, b, dist)
        
        
        rep = union_find.find(1)
        return union_find.getMinRoad(rep)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        