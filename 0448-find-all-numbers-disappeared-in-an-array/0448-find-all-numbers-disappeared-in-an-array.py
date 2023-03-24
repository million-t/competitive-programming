class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        index = 0
        
        while index < length:
            right_place = nums[index] - 1
            
            if right_place != index and nums[right_place] != nums[index]:
                nums[right_place], nums[index] = nums[index], nums[right_place]
                
            else:
                index += 1
        
        disappeared = []
        for ind, num in enumerate(nums):
            if num - 1 != ind:
                disappeared.append(ind + 1)
        
        return disappeared
        