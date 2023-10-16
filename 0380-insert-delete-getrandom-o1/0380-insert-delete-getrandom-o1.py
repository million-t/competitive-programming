class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.items = []

    def insert(self, val: int) -> bool:
        
        if val in self.indices:
            return False
        
        self.items.append(val)
        self.indices[val] = len(self.items) - 1
        
        return True
    

    def remove(self, val: int) -> bool:
        
        if val not in self.indices:
            return False
        
        index = self.indices[val]
        self.items[index] = self.items[-1]
        self.indices[self.items[index]] = index 
        self.items.pop()
        self.indices.pop(val)
        
        return True

    
    def getRandom(self) -> int:
        return random.choice(self.items)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()