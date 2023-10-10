class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.chain = {}
        self.tail = None
        
        
        

    def get(self, key: int) -> int:
        if key in self.chain:
            self.put(key, self.chain[key].val)
            return self.chain[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if not self.head:
            self.head = ListNode(key = key, val=value)
            self.tail = self.head
            self.chain[key] = self.head
            self.size += 1
        
        elif key in self.chain:
            node = self.chain[key]
            
            if self.tail == node:
                self.tail.val = value
            
            else:

                prev = node.prev
                next = node.next

                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
                node.val = value

                if prev:
                    prev.next = next
                    
                    if next:
                        next.prev = prev
                
                else:
                    if next:
                        next.prev = None
                        self.head = next
                    
                    else:
                        self.head = node
        
        elif self.size == self.capacity:
            popped_key = self.head.key
            self.chain.pop(popped_key)
            self.head = self.head.next
            
            
            if self.head:
                self.head.prev = None
                node = ListNode(key = key, val=value)
                self.tail.next = node
                node.prev = self.tail
                self.chain[key] = node
                self.tail = node
            
            else:
                self.head = ListNode(key = key, val=value)
                self.tail = self.head
                self.chain[key] = self.head
        
        else:
            node = ListNode(key = key, val=value)
            self.tail.next = node
            node.prev = self.tail
            self.chain[key] = node
            self.tail = node
            self.size += 1
            
            
            
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)