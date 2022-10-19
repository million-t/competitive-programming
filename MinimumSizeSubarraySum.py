class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix, curSum = [0], 0
        for num in nums:
            curSum += num
            prefix.append(curSum)
        output = 0
        l = 0
        for  r in range(1, len(prefix)):
            while prefix[r] - prefix[l] >= target:
                output = r - l if output == 0 else min(output, r - l)
                l += 1
        return output



            
