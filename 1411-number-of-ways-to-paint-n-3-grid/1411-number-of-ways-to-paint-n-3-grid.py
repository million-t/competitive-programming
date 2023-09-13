class Solution:
    def numOfWays(self, n: int) -> int:
        
        mod = 10**9 + 7
        fives = 6
        fours = 6
        
        for num in range(1, n):
            cur_fours = (fives*2 + fours*2)%mod
            cur_fives = (fives*3 + fours*2)%mod
            fives, fours = cur_fives, cur_fours
        
        return (fives + fours)%mod
        