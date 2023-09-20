class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        length = len(nums)
        suf = [0]*(length + 1)
        
        for ind in range(length - 1, -1, -1):
            suf[ind] = suf[ind + 1] + nums[ind]
        
        seen = {0:-1}
        pref = [0]
        ans = float('inf')
        
        for ind, num in enumerate(nums):
            pref.append(pref[-1] + num)
            dif = x - suf[ind]
            
            if dif in seen:
                ans = min(ans, seen[dif] + length - ind + 1)
                
            if pref[-1] == x:
                ans = min(ans, ind + 1)
            
            seen[pref[-1]] = ind
            
        return ans if ans != float('inf') else -1
        