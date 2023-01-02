class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])            
        return prefix_sums