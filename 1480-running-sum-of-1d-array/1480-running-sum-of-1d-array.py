class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        
        ps = []
        
        for num in nums:
            running_sum += num
            ps.append(running_sum)
        
        return ps