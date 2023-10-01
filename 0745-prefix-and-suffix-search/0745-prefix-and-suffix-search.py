class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = -1


class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for index, word in enumerate(words):
            cur = self.root
            
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                
                cur = cur.children[char]
            cur.isEnd = index

    def f(self, pref: str, suff: str) -> int:
        
        
        cur = self.root
        stack = []
        
        for char in pref:
            if char not in cur.children:
                return -1
                
            cur = cur.children[char]
            stack.append(char)
            
            
        
            
        def backtrack(node, stack):
            
            temp_ans = -1            
            
            if node.isEnd != -1:
                
                j = len(suff) - 1
                
                for ind in range(len(stack) - 1, -1, -1):
                    if j <= 0:
                        if j == 0 and suff[j] == stack[ind]: 
                            temp_ans = max(temp_ans, node.isEnd)
                            
                        break
                    
                    if suff[j] != stack[ind]:
                        break
                    
                    j -= 1    
            
            for char in node.children:
                stack.append(char)
                temp_ans = max(backtrack(node.children[char], stack), temp_ans)
                stack.pop()
            
            return temp_ans
                
        return max(-1, backtrack(cur, stack))
         
        
                    


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)