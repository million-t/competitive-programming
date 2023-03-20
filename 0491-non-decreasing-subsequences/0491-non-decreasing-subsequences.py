class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        sequences = []
        def backtrack(stack, index):
            nonlocal length
            
            if len(stack) > 1 and stack not in sequences:
                sequences.append(stack[:])
            
            if index >= length:
                return
            
            
            for i in range(index, length):
                
                if (not stack) or stack[-1] <= nums[i]:
                    stack.append(nums[i])
                    backtrack(stack, i + 1)
                    stack.pop()
            
        backtrack([], 0)
        
        
        return sequences
            