class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = -math.inf
        curSum = 0
        
        left = 0
        for right in range(len(nums)):
            curSum += nums[right]
            
            if right - left + 1 == k:
                maxSum = max(maxSum, curSum)
                curSum -= nums[left]
                left += 1
            
        return maxSum/k