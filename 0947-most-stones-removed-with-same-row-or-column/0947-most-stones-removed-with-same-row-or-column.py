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
    def removeStones(self, stones: List[List[int]]) -> int:
        
        row_stones = defaultdict(list)
        col_stones = defaultdict(list)
        
        for row, col in stones:
            row_stones[row].append((row, col))
            col_stones[col].append((row, col))
        
        union_find = DSU(stones)
        
        for row in row_stones:
            for pos in row_stones[row]:
                
                for stone in row_stones[row]:
                    union_find.union(pos, stone)        
                break
        
        for col in col_stones:
            for pos in col_stones[col]:
                
                for stone in col_stones[col]:
                    union_find.union(pos, stone)        
                break
        
        components = set()
        for x, y in stones:
            components.add(union_find.find((x, y)))
        
        return len(stones) - len(components)
        
        
        