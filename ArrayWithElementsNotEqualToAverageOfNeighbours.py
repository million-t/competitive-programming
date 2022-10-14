from math import ceil
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        mid = ceil(len(nums)/2)
        ans = [None]*len(nums)
        even = i = 0
        odd = 1
        while i < len(nums):
            if i >= mid:
                ans[odd] = nums[i]
                odd += 2
            else:
                ans[even] = nums[i]
                even += 2
            i+=1
        return ans
