class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        stack = []
        
        for direct in path:
            if direct in ['.', '']:
                continue
            
            elif direct == '..':
                if stack:
                    stack.pop()
                
            else:
                stack.append(direct)
                
            
        
        
        return '/' + '/'.join(stack)
                
        