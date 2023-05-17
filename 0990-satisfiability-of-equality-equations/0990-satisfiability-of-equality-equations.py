class DSU:
    def __init__(self):
        
        self.rep = {}
        self.rank = {}
        
        for _ord in range(ord('a'), ord('z') + 1):
            char = chr(_ord)
            self.rep[char] = char
            self.rank[char] = 1
    
    
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
    def equationsPossible(self, equations: List[str]) -> bool:
        
        
        union_find = DSU()
        
        for equation in equations:
            
            a, b, c, d = equation[0], equation[1], equation[2], equation[3]
            
            if b == '=':
                union_find.union(a, d)
        
        
        for equation in equations:
            a, b, c, d = equation[0], equation[1], equation[2], equation[3]
            
            if b == '!' and union_find.is_connected(a, d):
                return False
        
        return True
                
        
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        