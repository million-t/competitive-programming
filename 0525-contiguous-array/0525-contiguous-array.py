class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dif = 0
        ans = 0
        seen = {0:-1}
        
        
        for indx, bit in enumerate(nums):
            dif = dif + 1 if bit == 1 else dif - 1
            
            if dif in seen:
                ans = max(ans, indx - seen[dif])
            
            else:
                seen[dif] = indx
        
        return ans