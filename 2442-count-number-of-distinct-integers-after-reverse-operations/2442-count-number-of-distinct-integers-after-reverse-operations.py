class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            seen.add(num)
            seen.add(int(str(num)[::-1]))
            
        return len(seen)