class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.root = TrieNode()
        self.pending = deque()
        
        for word in words:
            cur = self.root
            
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                
                cur = cur.children[char]
            cur.isEnd = True
        

    def query(self, letter: str) -> bool:
        
        response = False
        self.pending.append(self.root)
        
        for _ in range(len(self.pending)):
            node = self.pending.popleft()
            
            if letter in node.children:
                self.pending.append(node.children[letter])
                
                if node.children[letter].isEnd:
                    response = True

        return response
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)