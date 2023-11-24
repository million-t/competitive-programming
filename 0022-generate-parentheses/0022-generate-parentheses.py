class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtrack(op, used, path):
            
            if not used and not op:
                ans.append(''.join(path))
                return
            
            
            if used:
                path.append('(')
                backtrack(op + 1, used - 1, path)
                path.pop()
            
            if op:
                path.append(')')
                backtrack(op - 1, used, path)
                path.pop()
        
        backtrack(0, n, [])
        return ans
            
               