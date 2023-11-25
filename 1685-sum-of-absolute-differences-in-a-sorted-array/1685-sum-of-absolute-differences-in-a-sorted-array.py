class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        
        total_sum = sum(nums)
        nums_size = len(nums)
        prefix_sums = []
        
        prefix = 0
        for num in nums:
            prefix_sums.append(prefix)
            prefix += num
            
        output = [0]*nums_size    
        for indx, val in enumerate(nums):
            output[indx] = val*(indx) - prefix_sums[indx] + (total_sum - val - prefix_sums[indx]) - val*(nums_size - indx - 1)
        
        return output 
        