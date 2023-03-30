class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        nums_xor = 0
        
        for num in nums:
            nums_xor ^= num
        
        
        visited = set()
        
        for num in nums:
        
            if num^nums_xor in visited:
                return [num, num^nums_xor]
            
            visited.add(num)
            
        