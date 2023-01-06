class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_indx = {}
        for indx, num in enumerate(nums):
            num_indx[num] = indx

        for old, new in operations:
            index = num_indx[old] 
            nums[index] = new
            num_indx[new] = index
            num_indx.pop(old)
        return nums
            
        
            
        
