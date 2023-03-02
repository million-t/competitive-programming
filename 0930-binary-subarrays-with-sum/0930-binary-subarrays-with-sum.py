class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        seen_diff = defaultdict(int)
        subarray_count = 0
        
        
        seen_diff[0] = 1
        for prefix in nums:
            diff = prefix - goal
            
            subarray_count += seen_diff[diff]
            seen_diff[prefix] += 1
        
        return subarray_count
            