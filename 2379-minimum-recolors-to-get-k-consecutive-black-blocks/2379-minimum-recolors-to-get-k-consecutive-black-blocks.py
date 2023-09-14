class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        left = 0
        whites = 0
        ops = float('inf')
        for right in range(len(blocks)):
            whites += int(blocks[right] == 'W')
            
            if right - left + 1 == k:
                ops = min(ops, whites)
                whites -= int(blocks[left] == 'W')
                left += 1
        
        return ops
        