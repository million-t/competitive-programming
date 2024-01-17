class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        
        _sum = 0
        count = 0
        
        for coin in sorted(coins):
            
            while _sum + 1 < coin:
                _sum += _sum + 1
                count += 1
            
            _sum += coin
        
        while _sum < target:
            _sum += _sum + 1
            count += 1
            
                
        return count
                
        