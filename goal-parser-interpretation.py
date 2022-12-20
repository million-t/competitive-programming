class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        for i, c in enumerate(command):
            if c == 'G':
                ans+= c
            elif c == ')':
                if command[i-1] == '(':
                    ans+='o'
                else:
                    ans+='al'
        return ans
