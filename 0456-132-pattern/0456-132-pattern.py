class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        medium_num = float('-inf')
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            
            if num < medium_num: 
                return True
            
            while stack and stack[-1] < num:
                medium_num = stack.pop()
            
            stack.append(num)
            
        return False    
                
        
            
                
            
                    
                