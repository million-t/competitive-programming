class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda : TrieNode())
        self.isEnd = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        root = TrieNode()
        
        for word in words:    
            cur = root
                        
            for char in word:
                cur = cur.children[char]
                cur.isEnd += 1
        
        ans = [] 
        for word in words:    
            cur = root
            path_sum = 0
            
            for char in word:
                cur = cur.children[char]
                path_sum += cur.isEnd
            
            ans.append(path_sum)
        
        
        return ans
        
            
        
        
                
        
        
        