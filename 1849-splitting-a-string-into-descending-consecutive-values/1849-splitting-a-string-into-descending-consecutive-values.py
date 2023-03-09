class Solution:
    def splitString(self, s: str) -> bool:
        
        
        stack = []
        found = False
        
        
        def is_found():
            
            if len(stack) < 2 or int(stack[-2]) - int(stack[-1]) != 1:
                return False
            
            
            return True
        
        
        
        
        def backtrack(number):
            nonlocal found
            
            if found:
                return 
            
            if not number:
                if is_found():
                    found = True
                    
                return
            
            for index in range(1, len(number) + 1):
                
                stack.append(number[:index])
                
                if len(stack) >= 2 and int(stack[-2]) - int(stack[-1]) != 1:
                    stack.pop()
                    continue
                    
                backtrack(number[index:])
                
                stack.pop()
        
                
        backtrack(s)
        
        return found