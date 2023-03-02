class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [-1]*k
        self.front = 0
        self.last = 0
        
        self.capacity = k
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        
        if self.size < self.capacity:
            self.arr[ self.front%self.capacity ] = value
            
            self.front -= 1
            if self.size == 0:
                self.last += 1
            
            self.size += 1
            return True
        
        return False
        

    def insertLast(self, value: int) -> bool:
        
        if self.size < self.capacity:
            self.arr[ self.last%self.capacity ] = value
            
            self.last += 1
            if self.size == 0:
                self.front -= 1
            
            self.size += 1
            return True
        
        return False

    def deleteFront(self) -> bool:
        
        if self.size > 0:
            self.arr[ (self.front + 1)%self.capacity ] = -1
            
            self.front += 1
            self.size -= 1
            
            if self.size == 0:
                self.last -= 1
            
            return True
        
        return False
        

    def deleteLast(self) -> bool:
        
        if self.size > 0:
            self.arr[ (self.last - 1)%self.capacity ] = -1
            
            self.last -= 1
            self.size -= 1
            
            if self.size == 0:
                self.front += 1
            
            return True
        
        return False
        

    def getFront(self) -> int:
        return self.arr[(self.front + 1)%self.capacity]
        

    def getRear(self) -> int:
        return self.arr[(self.last - 1)%self.capacity]
        

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()