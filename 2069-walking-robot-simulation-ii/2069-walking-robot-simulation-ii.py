class Robot:

    def __init__(self, width: int, height: int):
        
        self.valid = {}
        self.dir = {}
        i = 0
        for col in range(width):
            self.valid[i] = [col, 0]
            self.dir[i] = "East"
            i += 1
        
        for row in range(1, height):
            
            self.valid[i] = [width - 1, row]
            self.dir[i] = "North"
            i += 1
        
        for col in range(width - 2, -1, -1):
            self.valid[i] = [col, height - 1]
            self.dir[i] = "West"
            i += 1
        
        for row in range(height - 2, 0, -1):
            self.valid[i] = [0, row]
            self.dir[i] = "South"
            i += 1
        
        self.size = i
        self.pos = 0
        
        
    
    def step(self, num: int) -> None:
        self.pos = (num + self.pos) % self.size
        self.dir[0] = 'South'
        
                
         
    def getPos(self) -> List[int]:
        return self.valid[self.pos]
        

    def getDir(self) -> str:
        return self.dir[self.pos]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()