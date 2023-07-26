class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        
        def play(left, right):
            
            key = (left, right)
            if key in memo:
                return memo[key]
            
            if left + 1 == right:
                return max(piles[right], piles[left])
            
            if left == right:
                return piles[left]
            
            if left > right:
                return 0
            
            temp = play(left + 1, right - 1)
            take_first = min(play(left + 2, right), temp) + piles[left]
            take_last = min(play(left, right - 2), temp) + piles[right]
            memo[key] = max(take_first, take_last)
            return memo[key]
    
        
        max_score = play(0, len(piles) - 1)
        return max_score > sum(piles)/2