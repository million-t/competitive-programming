class Bitset:

    def __init__(self, size: int):
        self.bits = [0]*size
        self.set_count = 0
        self.size = size
        self.on = 1
        

    def fix(self, idx: int) -> None:
        if self.bits[idx] != self.on:
            self.set_count += 1
            self.bits[idx] = self.on

    def unfix(self, idx: int) -> None:
        if self.bits[idx] == self.on:
            self.set_count -= 1
            self.bits[idx] = 1 - self.on

    def flip(self) -> None:
        self.on = 1 - self.on
        self.set_count = self.size - self.set_count
            
        

    def all(self) -> bool:
        return self.set_count == self.size
        

    def one(self) -> bool:
        return bool(self.set_count)
        

    def count(self) -> int:
        return self.set_count
        

    def toString(self) -> str:
        rep = []
        for bit in self.bits:
            if bit == self.on:
                rep.append("1")
            
            else:
                rep.append("0")
                
        return "".join(rep)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()