class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        length = len(dominoes)
        right_fall = [0]*length
        left_fall = [(0, '')]*length
        
        prev_r = float('inf')
        for ind in range(length):
            if dominoes[ind] == 'R':
                prev_r = 0
            
            elif dominoes[ind] == 'L':
                prev_r = float('inf')
                
            right_fall[ind] = prev_r
            prev_r += 1 
        
        prev_l = float('inf')
        for ind in range(length - 1, -1, -1):
            if dominoes[ind] == 'L':
                prev_l = 0
            
            elif dominoes[ind] == 'R':
                prev_l = float('inf')
                
            left_fall[ind] = prev_l
            prev_l += 1
        
        
        ans = []
        for ind in range(length):
            right, left = right_fall[ind], left_fall[ind]
            
            if right == left:
                ans.append('.')
            
            elif right < left:
                ans.append('R')
            
            else:
                ans.append('L')
        
        return ''.join(ans)