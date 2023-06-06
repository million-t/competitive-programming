class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        xor = start^goal
        count = bin(xor).count('1')
        
        return count
        