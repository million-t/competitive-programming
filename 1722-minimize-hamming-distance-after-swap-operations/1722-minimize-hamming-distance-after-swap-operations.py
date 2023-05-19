class DSU:
    def __init__(self, nums):
        
        self.rep = {num: num for num in nums}
        self.rank = {num: 1 for num in nums}
    
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
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        n = len(source)
        union_find = DSU(range(n))
        
        for a, b in allowedSwaps:
            union_find.union(a, b)
        
        rep_val = defaultdict(dict)
        for ind, val in enumerate(source):
            rep = union_find.find(ind)
            rep_val[rep][val] = rep_val[rep].get(val, 0) + 1
        
        ans = 0
        for ind, num in enumerate(target):
            rep = union_find.find(ind)
            
            if num not in rep_val[rep]:
                ans += 1
            
            else:
                rep_val[rep][num] -= 1
                if not rep_val[rep][num]:
                    rep_val[rep].pop(num)
                
        
        return ans
        
                    
                    
                    
            
        
        
            
        
        
        
        