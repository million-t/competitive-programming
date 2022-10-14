class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        ans = 0
        for j in range(len(nums)):
            k += nums[j]
            while i<len(nums) and k < nums[j]*(j-i + 1):
                k-=nums[i]
                i+=1
            ans = max(ans,j-i+1)
        return ans 
