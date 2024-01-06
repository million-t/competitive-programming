class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        
        
        last_indx = {}
        for indx, num in enumerate(nums):
            last_indx[num] = indx
        
        mod = 10**9 + 7
        comps = 0
        lim = 0
        
        for indx, num in enumerate(nums):
            lim = max(last_indx[num], lim)
            
            if indx == lim:
                comps += 1
        
        return pow(2, comps - 1, mod)
        