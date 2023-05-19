class DSU:
    def __init__(self, words):
        
        self.rep = {word: word for word in words}
        self.rank = {word: 1 for word in words}
    
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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        seen = set()
        union_find = DSU(s1 + s2)
        for ind in range(len(s1)):
            union_find.union(s1[ind], s2[ind])
            seen.add(s1[ind])
            seen.add(s2[ind])
        
        
        rep_char = defaultdict(str)
        for char in seen:
            
            if rep_char[union_find.find(char)]:
                rep_char[union_find.find(char)] = min(rep_char[union_find.find(char)], char)
            
            else:
                rep_char[union_find.find(char)] = char
                
                
        ans = []
        for char in baseStr:
            if char in seen:
                rep = union_find.find(char)
                ans.append(rep_char[rep])
            
            else:
                ans.append(char)
        
        return ''.join(ans)
        
            
        
        
        
        
        