class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        
        for num in nums:
            arr[num-1] = 0
        
        left = 0
        for right in range(len(nums)):
            if arr[right]:
                arr[left] = right + 1
                left += 1
        
        return arr[:left]
        