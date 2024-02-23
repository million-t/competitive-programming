class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
        n = len(stones)
        if n == 1:
            return 0
        
        if k > n:
            return -1
        
        pref = [0]*(n + 1)
        
        for indx in range(n):
            pref[indx] = pref[indx - 1] + stones[indx]
        
        
        @cache
        def dp(left, right, cov):
            
            if cov == 1:
                if left == right:
                    return 0
                
                return dp(left, right, k)
            if left == right and cov == 1:
                return 0
            
            elif right - left + 1 == k and cov == 1:
                return pref[right] - pref[left - 1]
            
            if left == right or cov == 0:
                return float('inf')
            
            
            ans = dp(left + 1, right, cov - 1)
            for mid in range(left + k, right + 1):
                temp = dp(left, mid - 1, k) + dp(mid, right, cov - 1)
                ans = min(ans, temp)
            
            if cov == k:
                ans += pref[right] - pref[left - 1]
            
            return ans
        

        ans = dp(0, n - 1, k)
        return ans if ans != float('inf') else -1
        
        
        
                
                
        
        