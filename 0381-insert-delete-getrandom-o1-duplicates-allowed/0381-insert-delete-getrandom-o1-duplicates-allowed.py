class RandomizedCollection:

    def __init__(self):
        
        self.numbers = []
        self.indices = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        self.numbers.append(val)
        self.indices[val].add(len(self.numbers) - 1)
        return True if len(self.indices[val]) == 1 else False

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        
        
        target_indx = None
        for indx in self.indices[val]:
            target_indx = indx
            break
        
        self.indices[val].remove(target_indx)
        
        last_indx = len(self.numbers) - 1
        if last_indx in self.indices[self.numbers[-1]]:
            self.indices[self.numbers[-1]].remove(last_indx)
            self.indices[self.numbers[-1]].add(target_indx)
            
        self.numbers[last_indx], self.numbers[target_indx] = self.numbers[target_indx], self.numbers[last_indx]
        self.numbers.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.numbers)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()