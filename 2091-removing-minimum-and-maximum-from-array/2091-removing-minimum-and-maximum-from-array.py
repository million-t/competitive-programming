class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_ind = nums.index(min(nums))
        max_ind = nums.index(max(nums))
        
        length = len(nums)
        
        if min_ind == max_ind:
            return 1
        
        left_left = max(min_ind, max_ind) + 1
        right_right = max(length - min_ind, length - max_ind)
        left_right = min(min_ind, max_ind) + 1 + length - max(min_ind, max_ind)
        return min(left_left, right_right, left_right)
        