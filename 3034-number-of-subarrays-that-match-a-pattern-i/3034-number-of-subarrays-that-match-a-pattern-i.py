class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        ans = 0
        
        for indx in range(1, n):
            if indx + m > n:
                continue
               
            yes = 1
            for another_indx in range(indx, indx + m):
                if pattern[another_indx - indx] == 1 and nums[another_indx] > nums[another_indx - 1]:
                    continue
                elif pattern[another_indx - indx] == 0 and nums[another_indx] == nums[another_indx - 1]:
                    continue
                
                elif pattern[another_indx - indx] == -1 and nums[another_indx] < nums[another_indx - 1]:
                    continue
                
                else:
                    yes = 0
                    
            ans += yes
        
        return ans