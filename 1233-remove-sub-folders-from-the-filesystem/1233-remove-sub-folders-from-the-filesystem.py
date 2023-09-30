class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        
        
        root = TrieNode()
        for item in folder:
            
            fold = item.split('/')
            cur = root
            
            for f in fold:
                if f  not in cur.children:
                    cur.children[f] = TrieNode()
                
                cur = cur.children[f]
            cur.isEnd = True
        
        ans = []
        def dfs(node, path):
            if node.isEnd:
                ans.append('/'.join(path))
                return 
            
            for neigh in node.children:
                
                path.append(neigh)
                dfs(node.children[neigh], path)
                path.pop()
        dfs(root, [])
        return ans