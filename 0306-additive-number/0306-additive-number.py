class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        stack = []
        
        def backtrack(_slice):
            
            
            if not _slice:
                return True
            
            
            for i in range(1, len(_slice) + 1):
                new_slice = int(_slice[:i])
                
                if (len(stack) < 2 or stack[-1] + stack[-2] == new_slice) and \
                str(new_slice) == _slice[:i]:
                    
                    stack.append(new_slice)
                
                    if backtrack(_slice[i:]) and len(stack) > 2:
                        return True
    
                    stack.pop()
            
            return False
        
        
        return backtrack(num)