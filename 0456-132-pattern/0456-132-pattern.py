class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        two = float('-inf')
        stack = []
        
        for indx in range(len(nums) - 1, -1, -1):
            num = nums[indx]
            
            if num < two:
                return True
            
            while stack and num > stack[-1]:
                two = max(two, stack.pop())
            
            stack.append(num)
        
        return False