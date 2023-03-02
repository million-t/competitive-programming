class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        n = len(nums)
        
        result = [-1]*(n)
        stack = []
        
        for index in range(n):
            
            while stack and nums[stack[-1]] < nums[index]:
                result[stack.pop()] = nums[index]
            
            stack.append(index)
        
        return result[:n//2]
        