class DSU:
    def __init__(self, comps):
        
        self.rep = {tuple(comp): tuple(comp) for comp in comps}
        self.rank = {tuple(comp): 1 for comp in comps}
    
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        edges = []
        
        for ind, point_i in enumerate(points):
            xi, yi = point_i
            for j in range(ind + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, (point_i, points[j])))
        
        edges.sort()
        min_cost = 0
        union_find = DSU(points)
        
        for dist, nodes in edges:
            u, v = nodes
            u, v = tuple(u), tuple(v)
            if union_find.find(u) != union_find.find(v):
                min_cost += dist
                union_find.union(u, v)
        
        return min_cost
            
        
        
        