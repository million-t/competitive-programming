class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            
            mid = start + (end - start)//2
            cur_num = nums[mid]
            
            if cur_num == target:
                return mid
            
            elif cur_num > target:
                end = mid - 1
            
            else:
                start = mid + 1
            
        
        return -1