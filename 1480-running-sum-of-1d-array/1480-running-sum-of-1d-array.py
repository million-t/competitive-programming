class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sums = []
        prefix = 0
        for num in nums:
            prefix += num
            prefix_sums.append(prefix)
            
        return prefix_sums