class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum, postfixSum = 0, sum(nums) - nums[0]
        for i in range(len(nums)):
            if prefixSum == postfixSum:
                return i
            prefixSum += nums[i]
            postfixSum -= nums[i+1] if i < len(nums)-1 else 0
        return -1
