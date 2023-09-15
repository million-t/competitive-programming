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
        for ind, (start_x, start_y) in enumerate(points):
            for sec_ind in range(ind + 1, len(points)):
                end_x, end_y = points[sec_ind]
                dist = abs(start_x - end_x) + abs(start_y - end_y)
                edges.append((dist, (start_x, start_y), (end_x, end_y)))
            
        
        union_find = DSU(points)
        edges.sort()
        min_cost = 0
        
        for dist, start, end in edges:
            if not union_find.is_connected(start, end):
                union_find.union(start, end)
                min_cost += dist
        
        return min_cost
                
            
        