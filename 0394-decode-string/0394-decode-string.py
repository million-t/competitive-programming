class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(s):
            stack = []
            
            i = 0
            while i < len(s):
                
                if not s[i].isalpha():
                    num = ''
                    while i < len(s) and s[i].isnumeric():
                        num += s[i]
                        i += 1
                
                    inStack = []
                    if i < len(s) and s[i] == '[':
                        inStack.append(s[i])
                        i += 1
                    sub = ''
                    while inStack:
                        if s[i] == '[':
                            inStack.append(s[i])
                            sub += s[i]
                        elif s[i] == ']':
                            if len(inStack) > 1:
                                inStack.pop()
                                sub += s[i]

                            else:
                                if num:
                                    stack.append( int(num)*(helper(sub)))
                                else:
                                    stack.append( helper(sub))
                                inStack.pop()
                                break

                        else:
                            sub += s[i]

                        i += 1
                else:
                    stack.append(s[i])
                
                i += 1
            
            return ''.join(stack)
        return helper(s)
                
                
                
                    