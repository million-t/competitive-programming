class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        l = 0
        output = 0
        for r in range(len(s)):
            if r<k:
                if s[r] in 'aeiou':
                    count += 1
            else:
                if s[r] in 'aeiou':
                    count+=1
                if s[l] in 'aeiou':
                    count -= 1
                l+=1
            output = max(output, count)
        return output         
