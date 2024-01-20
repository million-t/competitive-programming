class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        
        pref = [0]
        for num in nums:
            pref.append(pref[-1] ^ num)
        
        seen = defaultdict(int)
        ans = 0
        
        for num in pref:
            ans += seen[num]
            seen[num] += 1
        
        return ans
        