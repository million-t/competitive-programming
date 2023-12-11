class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        ans = 0
        seen = defaultdict(int)
        
        
        for t in time:
            rem = t%60
            ans += seen[(60 - t)%60]
            seen[rem] += 1
        
        return ans
        