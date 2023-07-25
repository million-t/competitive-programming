class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0
        subsequences = 1
        
        for right in range(len(nums)):
            dif = nums[right] - nums[left]
            if dif > k:
                left = right
                subsequences += 1
            
            
        return subsequences