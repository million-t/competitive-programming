class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        comb = [(c, t) for c, t in zip(cost, time)]
        comb.sort(key = lambda x:(x[0], -x[1]))
        
        @cache
        def dp(indx, walls_left):
            
            if walls_left <= 0:
                return 0
            
            if indx >= len(comb):
                return float('inf')
            
            cos, tim = comb[indx]
            temp = dp(indx + 1, walls_left)
            temp = min(temp, dp(indx + 1, walls_left - tim - 1) + cos)
            
            return temp
        
        return dp(0, len(cost))
        
        
        return ans
        
        
        