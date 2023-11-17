class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        length = len(nums)
        nums.sort()
        ans = 0
        
        
        for indx  in range(length//2):
            ans = max(ans, nums[indx] + nums[length - indx - 1])
        
        return ans
        
        