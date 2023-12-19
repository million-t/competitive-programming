class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        
        target = len(set(nums))
        count = defaultdict(int)
        left = 0
        ans = 0
        
        for right, num in enumerate(nums):
            count[num] += 1
            
            while len(count) == target and count[nums[left]] - 1 != 0:
                count[nums[left]] -= 1
                left += 1
        
            if len(count) == target:
                ans += left + 1
        
        return ans
                
            
        
        