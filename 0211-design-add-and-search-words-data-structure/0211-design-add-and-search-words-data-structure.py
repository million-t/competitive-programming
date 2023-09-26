class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
        
        cur.isEnd = True

    def search(self, word: str) -> bool:
        
        def backtrack(start, node):
            cur = node
            
            for indx in range(start, len(word)):
                
                char = word[indx]
                if char == '.':
                    for node in cur.children.values():
                        if backtrack(indx + 1, node):
                            return True
                    
                    return False
                
                else:
                    if char not in cur.children:
                        return False
                    
                    cur = cur.children[char]
            
            return cur.isEnd
        
        return backtrack(0, self.root)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)