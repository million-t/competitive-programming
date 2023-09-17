class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                return mid
            
            s = nums[start]
            e = nums[end]
            m = nums[mid]
            if s < m and s <= target < m:
                end = mid - 1
            
            elif s > m and (target < m or target >= s):
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
            
            
        