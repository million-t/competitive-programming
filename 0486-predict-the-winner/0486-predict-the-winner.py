class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def recur(left, right):
            if left > right:
                return 0
            
            
            front = min(recur(left + 2, right), recur(left + 1, right - 1)) + nums[left]
            rear = min(recur(left + 1, right - 1), recur(left, right - 2)) + nums[right]
            return max(front, rear)
        
        return recur(0, len(nums) - 1)*2 >= sum(nums)
        