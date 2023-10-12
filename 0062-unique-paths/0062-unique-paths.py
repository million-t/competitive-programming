class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        _max = max(m - 1, n - 1)
        _min = min(m - 1, n - 1)
        
        ans = 1
        spots = _max + _min
        while spots > _max:
            ans *= spots
            spots -= 1
    
        
        return ans//factorial(_min)