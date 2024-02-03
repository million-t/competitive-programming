class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        
        @cache
        def dp(start):
            
            if start >= len(arr):
                return 0
            
            ans = 0
            cur_max = 0
            for indx in range(start, min(start + k, len(arr))):
                cur_max = max(cur_max, arr[indx])
                ans = max(ans, dp(indx + 1) + cur_max*(indx - start + 1))
            
            return ans
            
            
            
        return dp(0)