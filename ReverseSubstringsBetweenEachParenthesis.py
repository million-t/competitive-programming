class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                queue = []
                while stack[-1]!='(':
                    queue.append(stack.pop())
                stack.pop()
                while queue:
                    stack.append(queue.pop(0))    
            else:
                stack.append(s[i])
        ans = ''
        for c in stack:
            ans += c
        return ans
             
