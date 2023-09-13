class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        stack = []
        ans = 0
        
        for num in target:
            
            while stack and stack[-1] >= num:
                ans += stack.pop() - num
            
            if stack:
                stack[-1] = num
            
            else:
                stack.append(num)
        
        
        return ans + stack[-1] if stack else ans
        