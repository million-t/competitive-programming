class Node:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index>=self.size:
            return - 1
        cur = self.head
        i = 0
        while i<index:
            cur = cur.next
            i+=1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val,self.head)
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        if not cur: return self.addAtHead(val)
        while cur.next:
            cur = cur.next
        cur.next = Node(val,None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        elif index == self.size:
            return self.addAtTail(val)
        elif index > self.size:
            return -1
        else:   
            cur = self.head
            while index - 1:
                cur = cur.next
                index-=1
            tmp = cur.next
            cur.next = Node(val,tmp)
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return -1
        elif index == 0:
            self.head = self.head.next
            self.size-=1
        else:
            cur = self.head
            while index-1:
                cur = cur.next
                index-=1
            cur.next = cur.next.next
            self.size-=1






# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
