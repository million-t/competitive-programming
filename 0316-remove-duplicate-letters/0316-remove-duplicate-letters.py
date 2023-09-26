class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_indx = { char: indx for indx, char in enumerate(s) }
        added = set()
        stack = []
        
        for indx, char in enumerate(s):
            
            if char not in added:
                while stack and stack[-1] > char and last_indx[stack[-1]] > indx:
                    added.remove(stack.pop())
                
                stack.append(char)
                added.add(char)
        
        
        return ''.join(stack)
                    
        
        
        