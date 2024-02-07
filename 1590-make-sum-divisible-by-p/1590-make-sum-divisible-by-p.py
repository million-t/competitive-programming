class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums)%p
        
        if not target:
            return 0
        
        seen = defaultdict(int)
        seen[0] = -1
        run_sum = 0
        ans = float('inf')
        
        for indx, num in enumerate(nums):
            run_sum += num
            run_sum %= p
            dif = (run_sum - target)%p
            
            if dif in seen and indx - seen[dif] < len(nums):
                ans = min(ans, indx - seen[dif])
            
            seen[run_sum] = indx
        
        return ans if ans != float('inf') else -1
            
            
            
            
        