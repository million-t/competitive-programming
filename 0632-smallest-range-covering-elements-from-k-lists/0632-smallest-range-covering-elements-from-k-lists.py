class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        
        ptr = defaultdict(int)
        ans = [float('-inf'), float('inf')] 
        prev_min = float('-inf')
        
        for inner in range(sum(len(order) for order in nums)):
            _min = float('inf')
            _max = float('-inf')
            
            for indx in range(len(nums)):
                cur = ptr[indx]
                while cur < len(nums[indx]) and nums[indx][cur] == prev_min:
                    cur += 1
                
                ptr[indx] = cur
                if cur == len(nums[indx]):
                    return ans
                    
                _min = min(_min, nums[indx][cur])
                _max = max(_max, nums[indx][cur])
            
            if ans[1] - ans[0] > _max - _min :
                ans = [_min, _max]
                
            prev_min = _min
        
        return ans
                
            
            