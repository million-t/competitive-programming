class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        
        for i in range(k):
            currSum += nums[i]
        
        max_sum = currSum
        
        left = 0
        for right in range(k, len(nums)):
            currSum += nums[right] - nums[left] 
            
            max_sum = max(max_sum, currSum)
            left += 1
            
        return max_sum/k