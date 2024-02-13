class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        last = {s[i]: i for i in range(len(s))}
        seen = set()
        stack = []
        
        for indx, char in enumerate(s):
            
            if char not in seen:
                while stack and s[stack[-1]] > char and last[s[stack[-1]]] > indx:
                    seen.remove(s[stack.pop()])

                
                stack.append(indx)
                seen.add(char)

        for indx in range(len(stack)):
            stack[indx] = s[stack[indx]]
            
        return "".join(stack)