class DSU:
    def __init__(self, comps):
        
        self.rep = {comp: comp for comp in comps}
        self.rank = {comp: 1 for comp in comps}
        self.compSum = {comp: 0 for comp in comps}
        self.maxCompSum = 0
    
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
            self.compSum[rep_x] += self.compSum[rep_y]
            self.maxCompSum = max(self.maxCompSum, self.compSum[rep_x])
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
            self.compSum[rep_y] += self.compSum[rep_x]
            self.maxCompSum = max(self.maxCompSum, self.compSum[rep_y])
        else:
            self.rep[rep_y] = rep_x
            self.compSum[rep_x] += self.compSum[rep_y]
            self.maxCompSum = max(self.maxCompSum, self.compSum[rep_x])
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    
    def setCompSum(self, x, val):
        self.compSum[x] = val
        self.maxCompSum = max(self.maxCompSum, val) 
    
    def getMax(self):
        return self.maxCompSum
    

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        length = len(nums)
        union_find = DSU(range(length))
        ans = [0]*length
        connection = [0]*length
        
        
        for ind in range(length - 1, -1, -1):
            
            ans[ind] = union_find.getMax()
            target_ind = removeQueries[ind]
            right = target_ind + 1
            left = target_ind - 1
            
            union_find.setCompSum(target_ind, nums[target_ind])
            if right < length and connection[right]:
                union_find.union(target_ind, right)
            
            if left >= 0 and connection[left]:
                union_find.union(target_ind, left)
            
            
            connection[target_ind] = 1
        
        
        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        