class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count, good = {}, 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for val in count.values():
            if val>=2:
                good+=factorial(val)//(factorial(val-2)*2)
                
        return good