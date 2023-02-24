class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seen = {char: i for i, char in enumerate(s)}
        
        stack = []
        added = set()
        
        for i, char in enumerate(s):

            if char not in added:
                while stack and stack[-1] > char and last_seen[stack[-1]] > i:
                    added.remove(stack.pop())

                stack.append(char)
                added.add(char)
                
            
        return ''.join(stack)
                
        