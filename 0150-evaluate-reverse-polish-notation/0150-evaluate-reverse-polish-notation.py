class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            
            if token in '+-*/':
                
                if token=='-':
                    stack.append(-1*(stack.pop() - stack.pop()))
                    
                elif token == '/':
                    q, p = stack.pop(), stack.pop()
                    stack.append(int(p/q))
                    
                elif token == '+':
                    stack.append(stack.pop() + stack.pop())
                    
                elif token == '*':
                    stack.append(stack.pop()*stack.pop()) 
                    
            else:
                stack.append(int(token)) 
                
        return stack[0]