class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        space_indx = 0
        n = len(spaces)
        for i, letter in enumerate(s):
            if space_indx < n and i == spaces[space_indx]:
                ans += ' '
                space_indx += 1
            ans += letter
        return ans
            
            
            
        