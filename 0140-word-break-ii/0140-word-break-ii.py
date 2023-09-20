class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        wordDict = set(wordDict)
        def backtrack(ind, path, words):
            
            if ind >= len(s):
                
                temp = "".join(path)
                if temp in wordDict:
                    words.append(temp)
                    ans.append(" ".join(words))
                    words.pop()
                
                return
            
            path.append(s[ind])
            temp = "".join(path)
            if temp in wordDict:
                words.append(temp)
                backtrack(ind + 1, [], words)
                words.pop()
            
            backtrack(ind + 1, path, words)
        
        backtrack(0, [], [])
        return ans
                    
            
        