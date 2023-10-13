class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        length = len(nums)
        suff = [0]*(length + 1)
        
        for indx in range(length - 1, -1, -1):
            suff[indx] = (suff[indx + 1] + nums[indx])%p
        
        
        last_pos = defaultdict(lambda: float('-inf'))
        ans = float('inf')
        run_mod = 0
        
        
        for indx, num in enumerate(nums):
            left = last_pos[p - suff[indx]]
            run_mod = (run_mod + num)%p
                
            ans = min(ans, indx - left - 1)
            last_pos[run_mod] = indx
        
            if not run_mod:
                ans = min(ans, length - indx - 1)
                
            if not suff[indx]:
                ans = min(ans, indx)
        
        
        if ans == float("inf"):
            return -1
        
        return ans
            
            
            
        