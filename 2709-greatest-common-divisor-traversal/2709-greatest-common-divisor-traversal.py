
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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if 1 in nums and len(nums) > 1:
            return False
        

        nums = set(nums)
        dsu = DSU(range(max(nums) + 1))
        
        temp = []
        for num in nums:
            factor = 2
            tmp = num
            while factor*factor <= num:
                while not num%factor:
                    dsu.union(factor, tmp)
                    dsu.union(tmp//factor, tmp)
                    num //= factor
                    
                factor += 1
                
            if num > 1:
                dsu.union(num, tmp)
                if tmp > num:
                    dsu.union(tmp//num, tmp)
                
        reps = set()
        for num in nums:
            reps.add(dsu.find(num))
        # print(reps)
        return len(reps) == 1
        