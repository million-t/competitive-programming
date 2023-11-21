class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        negs = []
        pos = 1
        counted = False
        
        for num in nums:
            if num < 0:
                negs.append(num)
            
            elif num > 0:
                counted = True
                pos *= num
        

        if len(negs) > 1:
            negs.sort()
            
            if len(negs) % 2:
                negs.pop()
            
            for num in negs:
                pos *= num
            
            return pos
        
        elif counted:
            return pos
        
        return max(nums)