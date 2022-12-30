class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in nums:
            if not num%2:
                evenSum += num
        
        ans = []
        for val, ind in queries:
            prev_val = nums[ind]
            if not prev_val%2:
                evenSum -= prev_val
            nums[ind] += val
            if not nums[ind]%2:
                evenSum += nums[ind]
            ans.append(evenSum)
        return ans
