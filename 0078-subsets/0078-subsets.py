class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        power_set = []
        
        def backtrack(_set, index):
            nonlocal length
            
            power_set.append(_set[:])
            
            if index >= length:
                return
        
            
            for next_start in range(index, length):
                
                _set.append(nums[next_start])
                
                backtrack(_set, next_start + 1)
                
                _set.pop()
        
        backtrack([], 0)
        
        return power_set
        