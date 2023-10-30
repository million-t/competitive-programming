class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        
        @cache
        def dp(left, right):
            if left >= right - 1:
                return 0
            
            temp = float('inf')
            for mid in range(left + 1, right):
                temp = min(temp, dp(left, mid) + dp(mid, right))
            
            return temp + cuts[right] - cuts[left]
        
        
        return dp(0, len(cuts) - 1)
                
                
                
                
        