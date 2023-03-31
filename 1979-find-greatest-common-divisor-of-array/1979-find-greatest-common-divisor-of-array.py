class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        _min = min(nums)
        _max = max(nums)
        
        gcd = 1
        
        
        while _min:
            gcd = _min
            _min = _max%_min
            _max = gcd
        
        return gcd