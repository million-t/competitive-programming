class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        
        pref = [stones[0]]
        for indx in range(1, len(stones)):
            pref.append(pref[-1] + stones[indx])
        
        
        @cache    
        def dp(indx, person):
            
            if indx == len(pref) - 1:
                return pref[indx] if person == 'a' else -pref[indx]
            
            if person == 'a':
                ans = max(dp(indx + 1, 'a'), pref[indx] + dp(indx + 1, 'b'))
                return ans
            
            ans = min(dp(indx + 1, 'b'), dp(indx + 1, 'a') - pref[indx])
            return ans
            
        
        return dp(1, 'a')
            