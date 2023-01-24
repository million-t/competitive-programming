class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        positive_sum = 0
        max_sum = float("-inf")
        
        for num in nums:
            if positive_sum < 0:
                positive_sum = 0
            positive_sum += num
            max_sum = max(max_sum, positive_sum)
        
        return max_sum