class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        
        for indx, word in enumerate(words):
            cur = root
            
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                
                cur = cur.children[char]
            
            cur.isEnd = indx
            
        
        def inbounds(r, c): return 0 <= r < len(board) and 0 <= c < len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = set()
        
        def dfs(row, col, node, visited):
            
            if node.isEnd != -1:
                ans.add(node.isEnd)
                
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if inbounds(nr, nc) and (nr, nc) not in visited and board[nr][nc] in node.children:
                    visited.add((nr, nc))
                    dfs(nr, nc, node.children[board[nr][nc]], visited)
                    visited.remove((nr, nc))
                    
                    
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in root.children:
                    visited.add((row, col))
                    dfs(row, col, root.children[board[row][col]], visited)
                    visited.remove((row, col))
        
        fin_ans = []
        for indx in ans:
            fin_ans.append(words[indx])
        
        return fin_ans
            
            
            
            