class Solution:
    def rob(self, nums: List[int]) -> int:
        
        size = len(nums)
        if size < 2:
            return max(nums)
        
        memo = [0]*size
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        
        for ind in range(2, size):
            memo[ind] = max(memo[ind - 1], memo[ind - 2] + nums[ind])
        
        return max(memo[-1], memo[-2])
                
        