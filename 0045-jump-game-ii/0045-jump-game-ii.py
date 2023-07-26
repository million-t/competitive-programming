class Solution:
    def jump(self, nums: List[int]) -> int:
        
        length = len(nums)
        stack = [(length - 1, length - 1)]
        
        for ind in range(length - 2, -1, -1):
            jumps = nums[ind]    
            end = ind
            while stack and stack[-1][1] < min(ind + jumps, length - 1):
                start, end = stack.pop()

            stack.append((ind, end))
            
            
        return len(stack) - 1   
          