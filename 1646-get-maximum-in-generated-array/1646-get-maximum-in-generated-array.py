class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return n
        
        
        nums = [0, 1]
        
        for ind in range(2, n + 1):
            if ind%2:
                i = ind//2
                nums.append(nums[i] + nums[i + 1])
            
            else:
                nums.append(nums[ind//2])
        
        return max(nums)
                
                
        