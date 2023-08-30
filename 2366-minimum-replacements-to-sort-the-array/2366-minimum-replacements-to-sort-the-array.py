class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        
        prev = nums[-1]
        
        steps = 0
        for ind in range(len(nums) - 2, -1, -1):
            cur = nums[ind]
            
            if cur > prev:
                if prev:
                    inc = ceil(cur/prev)
                    steps += inc - 1                   
                    cur = cur//inc
                    
                    
                    
                    
            prev = cur
        
        return steps
                
            
        