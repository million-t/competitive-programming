class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_len = 0
        cur_sum = 0
        
        for num in nums:
            
            if not num:
                cur_sum = 0
            
            else:
                cur_sum += num
            
            max_len = max(max_len, cur_sum) 
    
        return max_len