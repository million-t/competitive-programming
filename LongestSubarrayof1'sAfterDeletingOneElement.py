class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        output, count = 0, 0
        for r in range(len(nums)):
            if nums[r]==0:
                count+=1
            while count > 1:
                if not nums[l]:
                    count-=1
                l += 1
            output = max(output,r-l)
        return output
                
                


        
                

        

