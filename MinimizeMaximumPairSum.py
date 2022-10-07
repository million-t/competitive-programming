class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = []
        for i in range(len(nums)//2 + 1):
            output.append(nums[i] + nums[len(nums)-1 - i])
        return max(output)  
