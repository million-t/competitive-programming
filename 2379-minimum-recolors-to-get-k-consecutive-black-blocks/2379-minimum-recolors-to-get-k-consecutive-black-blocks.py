class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        whites = 0
        left = 0
        min_op = float('inf')
        for right, color in enumerate(blocks):
            if color == 'W':
                whites += 1
            
            if right - left + 1 == k:
                min_op = min(min_op, whites)
                if blocks[left] == 'W':
                    whites -= 1
                
                left += 1
        
        return min_op
        
        