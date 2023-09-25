class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        stones.sort()
        
        @cache
        def dp(ind, path_sum):
            if ind >= len(stones):
                if path_sum < 0:
                    return float('inf')
                    
                return path_sum
            return min(dp(ind + 1, path_sum + stones[ind]), dp(ind + 1, path_sum - stones[ind]))
        
        
        return dp(0, 0)
            