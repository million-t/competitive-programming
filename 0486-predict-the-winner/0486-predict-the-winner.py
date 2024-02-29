class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def play(left, right):
            if left > right:
                return 0
            
            front = nums[left] + min(play(left + 2, right), play(left + 1, right - 1))
            rear = nums[right] + min(play(left + 1, right - 1), play(left, right - 2))
            return max(front, rear)
        
        return play(0, len(nums) - 1)*2 >= sum(nums)
        