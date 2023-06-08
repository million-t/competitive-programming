class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        nums.discard(0)
        
        return len(nums)