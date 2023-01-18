class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_val = 0
        
        for num in nums:
            xor_val ^= num
            
        return xor_val