class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0

        

        
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = TrieNode()
        
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()

                cur = cur.children[char]

            cur.isEnd += 1
        
        ord_a = ord('a')
        dp = {chr(ord_ + ord_a): [-1]*len(s) for ord_ in range(26)}
        
        for ind, char in enumerate(s):
            dp[char][ind] = ind
        
        for letter in dp:
            for ind in range(len(s) - 2, -1, -1):
                if dp[letter][ind] == -1:
                    dp[letter][ind] = dp[letter][ind + 1]
        
        
        def count(ind, node):
            
            ans = node.isEnd
            for char in node.children:
                if ind + 1 < len(s) and dp[char][ind + 1] != -1:
                    ans += count (dp[char][ind + 1], node.children[char])
            
            return ans
                
        
        return count(-1, root)