class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        valid_ips = []
        
        def backtrack(stack, substr):
            
            if len(stack) == 4 and not substr:
                valid_ips.append('.'.join(stack))
                return
            
            for ind in range(1, len(substr) + 1):
                
                _slice = substr[:ind]
                int_slice = int(_slice)
                
                if str(int_slice) == _slice and 0 <= int_slice <= 255:
                    
                    stack.append(_slice)
                    backtrack(stack, substr[ind:])
                    stack.pop()
                    
                else:
                    break
                
                
        
        backtrack([], s)
        
        return valid_ips
                
                
        