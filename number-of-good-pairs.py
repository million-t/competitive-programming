class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        ans, N = 0, len(nums)
        for i in range(N):
            for j in range(i+1,N):
                if nums[i] == nums[j]:
                    ans += 1
        return ans'''
        count, good = {}, 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for val in count.values():
            if val>=2:
                good+=factorial(val)//(factorial(val-2)*2)
        return good
