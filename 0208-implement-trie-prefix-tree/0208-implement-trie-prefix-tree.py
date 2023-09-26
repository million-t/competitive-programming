class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda :TrieNode())
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        cur = self.root
        for char in word:
            cur = cur.children[char]
        
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            
            cur = cur.children[char]
            
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            
            cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)