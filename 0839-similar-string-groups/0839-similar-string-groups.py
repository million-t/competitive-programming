

class DSU:
    def __init__(self, obj):
        
        self.rep = {num: num for num in obj}
        self.rank = {num: 1 for num in obj}
    
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        
        union_find = DSU(strs)
        
        for indx, word in enumerate(strs):
            for prev_indx in range(indx):
                
                dif = 0
                for i in range(len(word)):
                    if strs[prev_indx][i] != word[i]:
                        dif += 1
                
                if dif <= 2:
                    union_find.union(word, strs[prev_indx])
        
        reps = set()
        
        for word in strs:
            reps.add(union_find.find(word))
        
        return len(reps)
                    
                
            