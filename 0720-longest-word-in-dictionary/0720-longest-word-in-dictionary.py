class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        self.onPath = 0

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        root = TrieNode()
        
        for word in words:
            cur = root
            
            for char in word:
                indx = ord(char) - ord('a')
                if not cur.children[indx]:
                    cur.children[indx] = TrieNode()
                
                cur = cur.children[indx]
                cur.onPath += 1
            
            cur.isEnd = True
        
        
        
        ans = ""
        cur = root
        words.sort()
        temp = 0
        
        for word in words:
            
            cur = root
            level = 0
            end = 0
            
            for char in word:
                indx = ord(char) - ord('a')
                cur = cur.children[indx]
                end += int(cur.isEnd)
                level += 1
            
            if level == end and temp < level:
                ans = word
                temp = level
        
        return ans
                
            
            
            
        
        