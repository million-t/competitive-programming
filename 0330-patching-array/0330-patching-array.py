class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        patches = 0
        indx = 0
        pref = 0
        num = 1
        
        while num < n + 1:
            if pref > num:
                continue
                
            while indx < len(nums) and nums[indx] <= num and pref < num:
                pref += nums[indx]
                indx += 1
            
            if num > pref:
                pref += num
                patches += 1
            
            num = pref + 1
            
        
        return patches