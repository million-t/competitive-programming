class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        xor_sum = 0
        
        def backtrack(set_xor, index):
            nonlocal length, xor_sum
            
            xor_sum += set_xor
            
            if index >= length:
                return
        
            
            for next_start in range(index, length):
                
                set_xor ^= nums[next_start]
                
                backtrack(set_xor, next_start + 1)
                
                set_xor ^= nums[next_start]
        
        backtrack(0, 0)
        
        return xor_sum
        
        