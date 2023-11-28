class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        MOD = 10**9 + 7

        seatsTotal = corridor.count('S')
        if not (seatsTotal and seatsTotal%2 == 0):
            return 0

        result = 1
        for m in re.finditer(r'S(P*)S', corridor[corridor.find('S')+1:]):
            result *= len(m.group(1)) + 1
            result %= MOD

        return result
        