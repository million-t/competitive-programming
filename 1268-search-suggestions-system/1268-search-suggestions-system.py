class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        
        root = TrieNode()
        ord_a = ord('a')
        
        for product in products:
            cur = root
            
            for char in product:
                _ord = ord(char) - ord_a 
                if not cur.children[_ord]:
                    cur.children[_ord] = TrieNode()
                
                cur = cur.children[_ord]
            cur.isEnd = True
            
        
        def dfs(node, path):
            
            if len(temp) >= 3:
                return
            
            if node.isEnd:
                temp.append(''.join(path))
            
            
            for ind, child in enumerate(node.children):
                if child:
                    path.append(chr(ind + ord('a')))
                    dfs(child, path)
                    path.pop()
                    
        
        ans = []
        cur = root
        
        path = []
        for char in searchWord:
            _ord = ord(char) - ord_a 
            if not cur.children[_ord]:
                cur.children[_ord] = TrieNode()
                
            cur = cur.children[_ord]
            temp = []
            path.append(char)
            dfs(cur, path)
            ans.append(temp)
        
        return ans
        