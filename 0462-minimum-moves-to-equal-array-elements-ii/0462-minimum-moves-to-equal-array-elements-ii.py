class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        n = len(nums)
        suf = [0]*n
        nums.sort()
        prev = 0
        
        for indx in range(n - 2, -1, -1):
            dif = nums[indx + 1] - nums[indx]
            prev += dif * (n - indx - 1)
            suf[indx] = prev

        ans = suf[0]
        prev = 0
        
        for indx in range(1, n):
            dif = nums[indx] - nums[indx - 1]
            prev += dif * (indx)
            ans = min(ans, suf[indx] + prev)
        
        return ans
            
            
            
        