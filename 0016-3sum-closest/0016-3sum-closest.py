class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_sum = float("inf")
        length = len(nums)
        
        for ind, num in enumerate(nums):
            
            left = ind + 1
            right = length - 1
            
            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                
                _sum = num + num2 + num3
                if _sum > target:
                    right -= 1
                
                elif _sum < target:
                    left += 1
                
                else:
                    return target
                
                if abs(_sum - target) < abs(min_sum - target):
                    min_sum = _sum
            
        
        return min_sum
                
            