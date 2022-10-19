class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k < 0:
                if nums[l] == 0:
                    k += 1   
                l+=1
            output = max(output, r - l + 1)
        return output    
        
                
