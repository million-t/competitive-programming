class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        
        max_width = 0
        for indx, num in enumerate(nums):
            
            i = len(stack) - 1
            while i >= 0 and stack[i][0] <= num:
                max_width = max(max_width, indx - stack[i][1])
                i -= 1
                        
            if (stack and stack[-1][0] > num) or not stack:
                stack.append([num, indx])
        
        return max_width
        