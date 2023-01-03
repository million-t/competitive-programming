class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        def h_forward(piece):
            x, y = piece
        
            while y < 8:
                if [x, y] in queens:
                    
                    return [x, y]
                y += 1
            
            return []
        
        def h_backward(piece):
            x, y = piece
            
            while y >= 0:
                if [x, y] in queens:
                    
                    return [x, y]
                y -= 1
            
            return []
        
        def v_up(piece):
            x, y = piece
            
            while x >= 0:
                if [x, y] in queens:
                
                    return [x, y]
                x -= 1
            
            return []
        
        def v_down(piece):
            x, y = piece
            
            while x < 8:
                if [x, y] in queens:
                    
                    return [x, y]
                x += 1
            
            return []
        
        def d_l_up(piece):
            x, y = piece
            
            while x >= 0 or y >=0:
                if [x, y] in queens:
                    
                    return [x, y]
                x -= 1
                y -= 1
            
            return []
        
        def d_r_up(piece):
            x, y = piece
            
            while x >= 0 or y < 8:
                if [x, y] in queens:
                    
                    return [x, y]
                x -= 1
                y += 1
            
            return []
        def d_l_down(piece):
            x, y = piece
            
            while x < 8 or y >=0:
                if [x, y] in queens:
                    
                    return [x, y]
                x += 1
                y -= 1
            
            return []
        
        def d_r_down(piece):
            x, y = piece
            
            while x < 8 or y < 8:
                if [x, y] in queens:        
                    return [x, y]
                x += 1
                y += 1
                
            return []
                    
        attacking_pieces = [h_forward(king), h_backward(king), v_up(king), v_down(king), d_r_up(king), d_l_up(king), d_r_down(king), d_l_down(king)] #this might contain empty sets        
        
        real_attacking_pieces = []
        for piece in attacking_pieces:
            if piece:
                real_attacking_pieces.append(piece)
        
        return real_attacking_pieces