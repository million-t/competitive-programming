class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        ans = 0
        max_val = {}
        
        for num in nums:
            dig_sum = sum(map(int, str(num)))
            if dig_sum in max_val:
                ans = max(ans, num + max_val[dig_sum])
                max_val[dig_sum] = max(num, max_val[dig_sum])
            
            else:
                max_val[dig_sum] = num
        
        return ans if ans else -1
        