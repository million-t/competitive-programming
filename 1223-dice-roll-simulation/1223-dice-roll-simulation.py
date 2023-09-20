class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @cache
        def dp(cur, count, rolls):
            if rolls == n:
                return 1
            
            ans = 0
            for ind, _max in enumerate(rollMax):
                if ind == cur and count == _max:
                    continue
                
                elif ind == cur:
                    ans = (ans + dp(ind, count + 1, rolls + 1))%(10**9 + 7)
                
                else:
                    ans = (ans + dp(ind, 1, rolls + 1))%(10**9 + 7)
            
            return ans
        
        
        return dp(-1, 0, 0)
            