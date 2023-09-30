class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        two = float('-inf')
        stack = []
        
        for indx in range(len(nums) - 1, -1, -1):
            num = nums[indx]
            if num < two:
                return True
            
            while stack and stack[-1] < num:
                two = max(stack.pop(), two)
            
            stack.append(num)
            
        return False
        