class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        
        a = 0
        b = 0
        
        left = 0
        for right in range(len(colors)):
            
            if colors[right] != colors[left]:
                if colors[left] == 'A':
                    a += max(0, right - left - 2)
                
                else:
                    b += max(0, right - left - 2)
                    
                left = right
        
        
        if colors[left] == 'A':
            a += max(0, len(colors) - left - 2)

        else:
            b += max(0, len(colors) - left - 2)
        
        return True if a > b else False
        