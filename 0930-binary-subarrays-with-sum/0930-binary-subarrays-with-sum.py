class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        seen_diff = defaultdict(int)
        subarray_count = 0
        prefix = 0
        
        seen_diff[prefix] = 1
        for num in nums:
            
            prefix += num
            diff = prefix - goal
            
            subarray_count += seen_diff[diff]
            seen_diff[prefix] += 1
        
        return subarray_count
            