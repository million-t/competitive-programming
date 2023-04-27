
class LockingTree:

    def __init__(self, parent: List[int]):
        self.tree = [[] for _ in range(len(parent))]
        self.parents = {0: - 1}
        
        for child, par in enumerate(parent):
            if par != -1:
                self.tree[par].append(child)
                self.parents[child] = par
        
        self.locked = [0]*len(parent)
        
        
        

    def lock(self, num: int, user: int) -> bool:
        
        if not self.locked[num]:
            self.locked[num] = user
            return True
        
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        
        if self.locked[num]: 
            return False
        
        if self.locked[0]: 
            return False
        
        cur = num
        while cur != -1:
            if self.locked[cur]:
                return False
            
            cur = self.parents[cur]
            
        
        stack = [num]
        
        unlocks = 0
        while stack:
            cur = stack.pop()
            
            for child in self.tree[cur]:
                
                if self.locked[child]:
                    self.locked[child] = 0
                    unlocks += 1
                    
                stack.append(child)
        
        if not unlocks:
            return False
        
        self.locked[num] = user
        return True
                    


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)