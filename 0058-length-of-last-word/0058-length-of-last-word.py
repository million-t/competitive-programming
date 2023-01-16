class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = 0
        for left in range(len(s) - 1, -1, -1):
            if not right and s[left]!=' ':
                right = left
            if right and s[left]==' ':
                return right - left
            
            if right and left==0:
                return right - left + 1
        return 1