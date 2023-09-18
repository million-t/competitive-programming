class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        
        
        memo = {}

        def dp(ind):
            length = len(stoneValue)
            if ind >= length:
                return 0
                
            if ind in memo:
                return memo[ind]

            _max = min(dp(ind + 2), dp(ind + 3), dp(ind + 4)) + stoneValue[ind]
            if ind < length - 1:
                _max = max(_max, min(dp(ind + 3), dp(ind + 4), dp(ind + 5)) + stoneValue[ind] + stoneValue[ind + 1])
            
            if ind < length - 2:
                _max = max(_max, min(dp(ind + 4), dp(ind + 5), dp(ind + 6)) + stoneValue[ind] + stoneValue[ind + 1] + stoneValue[ind + 2])
            
            memo[ind] = _max
            return _max
        

        score = dp(0)
        _sum = sum(stoneValue)
        if score > _sum/2:
            return 'Alice'
        
        elif score < _sum/2:
            return 'Bob'
        
        return 'Tie'


        