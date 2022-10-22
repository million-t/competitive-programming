class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums)-1):
            prefix.append(nums[i]*prefix[-1])
        s = 1
        for i in range(len(prefix)-1, -1, -1):
            prefix[i] = prefix[i]*s
            s = s*nums[i]
        return prefix
