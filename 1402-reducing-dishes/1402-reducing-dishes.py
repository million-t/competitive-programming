class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse = True)
        additive = 0
        prev = 0
        cur_max = 0
        
        
        for sats in satisfaction:
            cur = prev + sats + additive
            cur_max = max(cur_max, cur)
            prev = cur
            additive += sats
        
        return cur_max