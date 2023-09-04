class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        
        longest = 0
        stack = [(')', 0)]
        
        for ind, char in enumerate(s):
            
            if char == ')' and stack and stack[-1][0] == '(':
                rec, pas = stack.pop()
                longest = max(longest, stack[-1][1] + pas + 2)
                stack[-1] = stack[-1][0], stack[-1][1] + pas + 2
                
            else:
                stack.append((char, 0))
        
        
        return longest
                    
                    
                    
                    
                
                
            