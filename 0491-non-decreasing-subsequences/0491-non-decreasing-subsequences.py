class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        sequences = []
        added = set()
        
        def backtrack(stack, index):
            nonlocal length
            
            if len(stack) > 1 and tuple(stack) not in added:
                sequences.append(stack[:])
                added.add(tuple(stack))
            
            for i in range(index, length):
                
                if (not stack) or stack[-1] <= nums[i]:
                    stack.append(nums[i])
                    backtrack(stack, i + 1)
                    stack.pop()
            
            
        backtrack([], 0)
        
        return sequences
            