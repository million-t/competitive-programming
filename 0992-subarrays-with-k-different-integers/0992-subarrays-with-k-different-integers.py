class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        count = defaultdict(int)
        count1 = defaultdict(int)
        ans = 0
        left = 0
        mid = 0
        
        for right, num in enumerate(nums):
            
            count[num] += 1
            count1[num] += 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                
                if left == mid:
                    count1[nums[mid]] -= 1
                    if not count1[nums[mid]]:
                        count1.pop(nums[mid])
                    
                    mid += 1
                
                if not count[nums[left]]:
                    count.pop(nums[left])
                
                left += 1
            
            while count1[nums[mid]] > 1:
                count1[nums[mid]] -= 1
                mid += 1
            
            
            if len(count) == k and len(count1) == k:
                ans += mid - left + 1
            
        
        return ans
        