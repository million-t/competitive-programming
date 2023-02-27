class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        for i in range(1, n):
            nums[i] += nums[i - 1]
            
        diff_map = {0:1}
        
        count = 0 
        for prefix in nums:
            diff = prefix - k
            count += diff_map.get(diff, 0)
            
            diff_map[prefix] = diff_map.get(prefix, 0) + 1
            
        return count



