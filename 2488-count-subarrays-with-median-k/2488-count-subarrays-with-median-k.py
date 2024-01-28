class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        target = nums.index(k)
        seen = defaultdict(int)
        
        state = 0
        for indx in range(target, -1, -1):
            num = nums[indx]
            if num > k:
                state += 1
            
            elif num < k:
                state -= 1
                
            seen[state] += 1
        
        ans = 0
        state = 0
        
        for indx in range(target, len(nums)):
            num = nums[indx]
            if num > k:
                state += 1
            
            elif num < k:
                state -= 1
            
            wanted = -state
            wanted2 = 1 - state 
            ans += seen[wanted]
            ans += seen[wanted2]
       
        return ans