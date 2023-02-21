class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head
        

    def visit(self, url: str) -> None:
        self.current.next = Node(url, self.current)
        self.current = self.current.next
        

    def back(self, steps: int) -> str:
        
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        
        return self.current.val 
        

    def forward(self, steps: int) -> str:
        
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        
        return self.current.val 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)