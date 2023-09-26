class TrieNode:
    def __init__(self):
        self.children = {}
        self.endVal = 0
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, key: str, val: int) -> None:
        
        cur = self.root
        stack = []
        
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
                
            stack.append(cur)
            cur = cur.children[char]
        
        subt = 0
        add = 0
        if cur.endVal > 0:
            subt = cur.endVal
        
        cur.value += val - subt
        cur.endVal = val
            
        while stack:
            stack.pop().value += val - subt
            
        

    def sum(self, prefix: str) -> int:
        
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            
            cur = cur.children[char]
        
        return cur.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)