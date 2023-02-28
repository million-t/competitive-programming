class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        all_req = [0]*(n + 1)
        
        for start, end in requests:
            all_req[start] += 1
            all_req[end + 1] -= 1
        
        all_req[0] = [all_req[0], 0]
        for i in range(1, n + 1):
            all_req[i] = [all_req[i] + all_req[i - 1][0], i]
        
        all_req.pop()
        all_req.sort()
        nums.sort()
        
        for i in range(n):
            all_req[i][0] = nums[i]
        for i in range(n):
            nums[all_req[i][1]] = all_req[i][0]
            
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        max_sum = 0
        for start, end in requests:
            
            if start:
                max_sum += nums[end] - nums[start - 1]
            
            else:
                max_sum += nums[end]
        
        
        return max_sum % (10**9 + 7)
            
            
        