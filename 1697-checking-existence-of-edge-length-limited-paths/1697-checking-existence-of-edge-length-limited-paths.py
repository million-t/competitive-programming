class DSU:
    def __init__(self, comps):
        
        self.rep = {comp: comp for comp in comps}
        self.rank = {comp: 1 for comp in comps}
        self.maxDist = {comp: 0 for comp in comps}
    
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
            return
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
            self.maxDist[rep_x] = max(self.maxDist[rep_x], self.maxDist[rep_y], dist)
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
            self.maxDist[rep_y] = max(self.maxDist[rep_x], self.maxDist[rep_y], dist)
        
        else:
            self.rep[rep_y] = rep_x
            self.maxDist[rep_x] = max(self.maxDist[rep_x], self.maxDist[rep_y], dist)
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getMax(self, x):
        return self.maxDist[self.find(x)]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        
        
        for ind, query in enumerate(queries):
            x, y, lim = query
            queries[ind] = (lim, x, y, ind)
        
        edgeList.sort(key=lambda x:x[-1])
        queries.sort()
        
        length = len(queries)
        ans = [False]*length
        union_find = DSU(range(n))
        ind = 0
        
        for u, v, dist in edgeList:
            
            while ind < length and queries[ind][0] <= dist:
                lim, x, y, i = queries[ind]
                if union_find.is_connected(x, y):
                    ans[i] = True
                
                ind += 1
                
            if not union_find.is_connected(u, v):
                union_find.union(u, v, dist)
        
        while ind < length:
            lim, x, y, i = queries[ind]
            if union_find.is_connected(x, y):
                ans[i] = True

            ind += 1
        
        return ans
            
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        