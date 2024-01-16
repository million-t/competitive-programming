class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        bits = k
        for num in nums:
            bits ^= num
        
        return bits.bit_count()
        
        