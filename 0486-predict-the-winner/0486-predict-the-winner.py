class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def maximize(left, right):
            if left > right:
                return 0
            
            if left == right:
                return nums[left]
            
            go_with_left = nums[left] + min(maximize(left + 1, right - 1), maximize(left + 2, right))
            go_with_right = nums[right] + min(maximize(left, right - 2), maximize(left + 1, right - 1))
            
            return max(go_with_left, go_with_right)
        
        total_score = sum(nums)
        
        left = 0
        right = len(nums) - 1
        
        player1_score = maximize(left, right)
        
        return player1_score >= total_score/2
        
        