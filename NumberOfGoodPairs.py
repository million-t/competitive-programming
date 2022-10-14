class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans, N = 0, len(nums)
        for i in range(N):
            for j in range(i+1,N):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
