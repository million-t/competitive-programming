class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        nums.sort()
        
        _gcd = 0
        for num in numsDivide:
            _gcd = gcd(_gcd, num)
            
        
        for ind in range(len(nums)):
            if not _gcd % nums[ind]:
                return ind
        
        return -1