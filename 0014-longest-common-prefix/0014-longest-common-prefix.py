class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda :TrieNode())
        self.isEnd = False
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        root = TrieNode() 
        
        for word in strs:
            
            if not word:
                return ""
            
            cur = root
            for char in word:
                cur = cur.children[char]
            
            cur.isEnd = True
            
        
        ans = []
        
        cur = root
        while len(cur.children) == 1:
            
            if cur.isEnd:
                    return ''.join(ans)
            
            for char in cur.children:
                ans.append(char)
                
                cur = cur.children[char]
                
        return ''.join(ans)