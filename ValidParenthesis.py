class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingPar, closingPar = '([{', ')]}'
        if len(s) == 1:
            return False 
        for character in s:
            if character in openingPar:
                stack.append(character)
            elif character in closingPar:
                if not stack:
                    return False
                elif stack[-1] == openingPar[closingPar.index(character)]:
                    stack.pop()
                else:
                    return False
        return False if stack else True
