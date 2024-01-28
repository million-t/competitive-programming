class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        pref = [nums[0]]
        pref_sum = [nums[0]]
        for indx in range(1, len(nums)):
            pref.append(max(pref[-1], nums[indx]))
            pref_sum.append(pref_sum[-1] + nums[indx])
        
        @cache
        def dp(start, k):
            if start < 0:
                return 0
            
            if k == 1:
                return pref_sum[start]
            
            if k == start + 1:
                return pref[start]
            
            ans = float("inf")
            run_sum = 0
            for indx in range(start, k - 2, -1):
                run_sum += nums[indx]
                ans = min(ans, max(run_sum, dp(indx - 1, k - 1)))
            
            return ans
            
        
        return dp(len(nums) - 1, k)