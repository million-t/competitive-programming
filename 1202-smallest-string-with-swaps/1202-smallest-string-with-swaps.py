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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        union_find = DSU(len(s))
        for a, b in pairs:
            union_find.union(a, b)
        
        rep_char = defaultdict(list)
        rep_ind = defaultdict(list)
        
        ans = ['']*len(s)
        for ind, char in enumerate(s):
            rep_char[union_find.find(ind)].append(char)
            rep_ind[union_find.find(ind)].append(ind)
        
        
        for rep, chars in rep_char.items():
            chars.sort(reverse = True)
            
            indices = rep_ind[rep] 
            for char in chars:
                ans[indices.pop()] = char
        
        return ''.join(ans)
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        