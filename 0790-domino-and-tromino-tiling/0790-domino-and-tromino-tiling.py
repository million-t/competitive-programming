class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        
        MOD = 10**9 + 7
        top = [0]*(n + 1)
        bottom = [0]*(n + 1)
        both = [0]*(n + 1)
        
        top[2] = bottom[2] = 1
        both[1] = 1
        both[2] = 2
        
        for num in range(3, n + 1):
            top[num] += (both[num - 2] + bottom[num - 1])%MOD
            bottom[num] += (both[num - 2] + top[num - 1])%MOD
            both[num] += (top[num - 1] + bottom[num - 1] + both[num - 1] + both[num - 2])%MOD
        
        
        
        return both[-1]
        