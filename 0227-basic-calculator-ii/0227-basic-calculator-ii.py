class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        
        temp = []
        
        indx = 0
        while indx < len(s):
            
            if not s[indx].isnumeric():
                temp.append(s[indx])
                indx += 1
                continue
            
            num = []
            while indx < len(s) and s[indx].isnumeric():
                num.append(s[indx])
                indx += 1
            
            temp.append("".join(num))
        
        s = temp
        
        
        
        
        
        stack = []
        for indx in range(len(s) - 1, -1, -1):
            if s[indx] == '-':
                stack.append(-stack.pop())
            
            elif s[indx] not in '/*+':
                stack.append(int(s[indx]))
            
            elif s[indx] in '/*':
                stack.append(s[indx])
        
        
        stack.reverse()
        another_stack = []
        
        for indx in range(len(stack)):
            if another_stack and another_stack[-1] == '/':
                another_stack.pop()
                num1 = another_stack.pop()
                num2 = stack[indx]
                quot = 0
                
                if num1*num2 < 0:
                    quot = -(abs(num1)//abs(num2))    
                
                else:
                    quot = num1//num2
                    
                another_stack.append(quot)
                
            elif another_stack and another_stack[-1] == '*':
                another_stack.pop()
                num1 = another_stack.pop()
                num2 = stack[indx]
                
                prod = num1*num2
                another_stack.append(prod)
            
            else:
                another_stack.append(stack[indx])
            
        
        return sum(another_stack)
                
                