class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def helper(text):
            
            stack = []
            for char in text:

                if char == '#':
                    if stack:
                        stack.pop()

                else:
                    stack.append(char)
            
            return ''.join(stack)
        
        return helper(s) == helper(t)
    