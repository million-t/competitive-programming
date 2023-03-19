class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        window_size = length - k
        
        left = 0
        win_sum = 0
        min_win_sum = float('inf')
        
        for right, point in enumerate(cardPoints):
            win_sum += point
            
            if right - left + 1 == window_size:
                min_win_sum = min(min_win_sum, win_sum)
                win_sum -= cardPoints[left]
                left += 1
        
        
        _sum = sum(cardPoints)
        
        if min_win_sum == float('inf'):
            return _sum
        
        return _sum - min_win_sum
            
        