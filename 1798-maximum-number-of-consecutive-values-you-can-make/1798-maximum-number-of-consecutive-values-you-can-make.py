class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        pref = 0
        
        coins.sort()
        for num in coins:
            if pref + 1 < num:
                return pref + 1
            
            pref += num
        
        return pref + 1
        