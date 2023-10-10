class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        ops = {
            'n': {
                'G': (-1, 0),
                'L': 'w',
                'R': 'e'
            },
            'e': {
                'G': (0, 1),
                'L': 'n',
                'R': 's'
            },
            's': {
                'G': (1, 0),
                'L': 'e',
                'R': 'w'
            },
            'w': {
                'G': (0, -1),
                'L': 's',
                'R': 'n'
            }
            
        }
        
        face = 'n'
        row, col = 0, 0
        
        for char in instructions:
            if char == "G":
                dr, dc = ops[face]["G"]
                row += dr
                col += dc
                
            else:
                face = ops[face][char]
                        
        return (row, col) == (0, 0) or face != 'n'
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                    
                
                        
        
        