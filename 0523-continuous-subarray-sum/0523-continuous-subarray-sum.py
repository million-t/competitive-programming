class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        seen = defaultdict(lambda : len(nums))
        seen[0] = -1
        pref = 0
        
        for indx, num in enumerate(nums):
            pref += num
            mod = pref%k
            prev = seen[mod]
            if seen[mod] + 1 < indx:
                return True
            
            seen[mod] = min(seen[mod], indx)
        
        return False
        
        