class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        single = 0
        paired = 0
        
        for num in nums:
            
            single ^= num
            single &= ~paired
            
            paired ^= num
            paired &= ~single
        
        return single
        