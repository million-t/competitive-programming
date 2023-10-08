class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        
        target = nums[0]
        for num in nums:
            target &= num
        
        if target:
            return 1
        
        length = len(nums)
        suff = [0]*length
        prev_and = nums[-1]
        
        for indx in range(length - 2, -1, -1):
            suff[indx] = prev_and
            prev_and &= nums[indx]
        
        count = 0
        pref = nums[0]
        for indx, num in enumerate(nums):
            pref &= num
            if not pref and not suff[indx]:
                count += 1
                
                if indx < length - 1:
                    pref = nums[indx + 1]
        
        return count
                
            
            
        