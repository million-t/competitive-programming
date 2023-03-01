class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(char)
            
            else:
                inner = 0
                
                while stack and stack[-1] != '(':
                    inner += stack.pop()
                
                stack.pop()
                stack.append(max(1, 2*inner))
                
        
        return sum(stack)