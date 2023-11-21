class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        count = 0
        mod = 10**9 + 7
        seen = defaultdict(int)
        
        for num in nums:
            rev = int(str(num)[::-1])
            dif = num - rev
            count += seen[dif]
            count %= mod
            seen[dif] += 1
        
        return count
            
        