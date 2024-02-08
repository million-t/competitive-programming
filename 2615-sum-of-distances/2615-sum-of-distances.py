class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        
        pref = defaultdict(lambda : [0, 0])
        ans = [0]*len(nums)
        
        for indx, num in enumerate(nums):
            ans[indx] = pref[num][0]*indx - pref[num][1]
            pref[num][0] += 1
            pref[num][1] += indx
        
        suf = defaultdict(lambda : [0, 0])
        for indx in range(len(nums) - 1, -1, -1):
            num = nums[indx]
            ans[indx] += suf[num][1] - suf[num][0]*indx
            suf[num][0] += 1
            suf[num][1] += indx
        
        return ans
            