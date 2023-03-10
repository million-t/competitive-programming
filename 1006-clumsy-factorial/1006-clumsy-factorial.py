class Solution:
    def clumsy(self, n: int) -> int:
        op = {
            0:'*',
            1:'//',
            2:'+',
            3:'-'
        }
        
        expression = []
        
        for i in range(n):
            expression.append(str(n - i))
            
            if i < n - 1:
                expression.append(op[i%4])
            
            
        return eval(''.join(expression))
        