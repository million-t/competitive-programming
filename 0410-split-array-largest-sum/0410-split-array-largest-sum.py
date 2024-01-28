class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(target):
            cur_sum = 0
            count = 1
            
            for num in nums:
                cur_sum += num
                
                if cur_sum > target:
                    count += 1
                    cur_sum = num
            
            return count
        
        
        
        start = max(nums)
        end = sum(nums)
        
        while start <= end:
            mid = start + (end - start)//2
            
            count = check(mid)
            if count <= k:
                end = mid - 1
            
            else:
                start = mid + 1
                
        
        
        return start