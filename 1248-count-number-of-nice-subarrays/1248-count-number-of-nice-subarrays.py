class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice = 0
        odd_count = 0   
        left = 0
        
        evens = 1
        
        for right in range(len(nums)):
            if nums[right]%2:
                odd_count += 1
            
            while odd_count > k:
                if nums[left]%2:
                    odd_count -= 1
                    evens = 1
                
                left += 1
                    
            while odd_count == k and not nums[left]%2:
                evens += 1
                left += 1
            
            if odd_count == k:
                nice +=  evens
                
        return nice