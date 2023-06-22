class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        right = 0
        mean = []
        
        while right < length:
            
            left = right
            win_sum = 0
            while right < length - 1 and nums[right] <= nums[right + 1]:
                win_sum += nums[right]
                right += 1
            
            
            cur_sum = win_sum + nums[right]
            cur_range = right - left + 1
            cur_mean = cur_sum/cur_range
            
            while mean and mean[-1][0] < cur_mean:
                prev_mean, prev_range = mean.pop()
                cur_range += prev_range
                cur_sum = (prev_mean*prev_range + cur_sum)
                cur_mean = cur_sum/cur_range
            
            mean.append((cur_mean, cur_range))
            
            right += 1
        
        _max = float('-inf')
        for val, _range in mean:
            _max = max(_max, ceil(val))
        
        return _max
        