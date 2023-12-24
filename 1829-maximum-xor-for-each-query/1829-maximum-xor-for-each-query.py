class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        
        pref = [nums[0]]
        for indx in range(1, len(nums)):
            pref.append(pref[-1] ^ nums[indx])
        
        mask = 0
        while maximumBit:
            mask <<= 1
            mask ^= 1
            maximumBit -= 1
        
        ans = []
        while pref:
            temp = pref.pop()
            ans.append(mask & (~temp))
        
        return ans
        
        