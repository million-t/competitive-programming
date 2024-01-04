class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        freq = Counter(nums)
        
        for num, count in freq.items():
            if count == 1:
                return -1
            
            q = math.ceil(count / 3)
            ops += q
        
        return ops