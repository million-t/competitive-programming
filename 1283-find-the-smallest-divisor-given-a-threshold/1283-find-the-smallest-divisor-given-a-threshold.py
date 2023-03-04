class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def sum_when_divided_by(n):
            _sum = 0
            
            for num in nums:
                _sum += ceil(num/n)
            
            return _sum
        
        
        
        start = 1
        end = max(nums)
        divisor = 0
        
        while start <= end:
            mid = start + (end - start)//2
            
            cur_div_sum = sum_when_divided_by(mid)
            
            if cur_div_sum <= threshold:
                divisor = mid
                end = mid - 1
        
            else:
                start = mid + 1
            
        return start