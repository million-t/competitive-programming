class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        dp = [(1, 1)]
        for ind in range(1, len(nums)):
            cur = nums[ind]
            prev = nums[ind - 1]
            
            
            if prev < cur:
                dp.append((dp[-1][1] + 1, dp[-1][1]))
            
            if prev > cur:
                dp.append((dp[-1][0], dp[-1][0] + 1))
        
        return max(dp[-1])
            
                
        
        
            
        